from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .services.api_prestador import ApiPrestadorExportaDados
from .services.api_clientes import ApiClienteExportaDados
from .services.api_externas.api_cep import apiGetCep
from .services.api_soc.exporta_dados_user import ApiUserExporta
from .services.api_soc.api_prestador_soap_soc import send_web_service_soc
from .services.api_senior.web_service_fornecedor_senior_cadastro import web_service_post_prestadores
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
import json


@login_required(login_url='login')
def index(request):
    return render(
        request,
        'task/index.html'
    )


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'task/partials/dashboard.html')


@login_required(login_url='login')
def agendamento(request):
    return render(request, 'task/partials/agendamento.html')


@login_required(login_url='login')
def form_db(request):
    
    return render(
        request,
        'task/senior.html')


@login_required(login_url='login')
def form_prestador(request):
    
    return render(
        request,
        'task/prestador.html')


@login_required(login_url='login')
def buscar_prestador(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        
        if cnpj:
            api_prestadores = ApiPrestadorExportaDados(cnpj)
            prestadores_dados = api_prestadores.api_prestador_soc()

            if prestadores_dados and isinstance(prestadores_dados, list):
                
                if len(prestadores_dados) > 1:
                    return JsonResponse({'options': prestadores_dados})

                # Caso haja apenas um prestador
                nome_prestador = prestadores_dados[0].get('nome', 'Nome não encontrado')
                codigo_prestador = prestadores_dados[0].get('codigo', 'Nome não encontrado')
                return JsonResponse({'nome_prestador': nome_prestador, 'codigo': codigo_prestador})

        return JsonResponse({'nome_prestador': 'Prestador não encontrado'}, status=404)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

@login_required(login_url='login')
def buscar_cliente(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        
        if cnpj:
            api_prestadores = ApiClienteExportaDados(cnpj)
            cliente_dados = api_prestadores.api_prestador_soc()

            if cliente_dados and isinstance(cliente_dados, list):
                
                if len(cliente_dados) > 1:
                    return JsonResponse({'options': cliente_dados})

                # Caso haja apenas um prestador
                nome_cliente = cliente_dados[0].get('nome', 'Nome não encontrado')
                codigo_cliente = cliente_dados[0].get('codigo', 'Nome não encontrado')
                return JsonResponse({'nome_cliente': nome_cliente, 'codigo': codigo_cliente})

        return JsonResponse({'nome_cliente': 'Cliente não encontrado'}, status=404)

    return JsonResponse({'error': 'Método não permitido'}, status=405)


@login_required(login_url='login')
def send_request_senior_odc(request):
    if request.method == 'POST':
        all_data = request.POST.dict()
        
        if all_data:

            prestador_info = all_data.get('nome-prestador', '')
            cliente_info = all_data.get('input-cliente', '')
            
            if prestador_info:

                index = prestador_info.find(' - ')

                if index != -1:

                    codigo = prestador_info[:index].strip()
                    nome_prestador = prestador_info[index + 3:].strip()
                else:
                    codigo = prestador_info
                    nome_prestador = ''

                all_data['codigo_prestador'] = codigo
                all_data['nome_prestador'] = nome_prestador

                del all_data['nome-prestador']
            
            
            if cliente_info:

                index = cliente_info.find(' - ')

                if index != -1:

                    codigo = cliente_info[:index].strip()
                    nome_cliente = cliente_info[index + 3:].strip()
                else:
                    codigo = cliente_info
                    nome_prestador = ''

                all_data['codigo_cliente'] = codigo
                all_data['nome_cliente'] = nome_cliente

                del all_data['input-cliente']
            
            print(all_data)
            
            return JsonResponse({
                'message': 'Dados enviados com sucesso', 
                'data': all_data
            }, status=200)
        
        return JsonResponse({'message': 'Nenhum dado recebido'}, status=200)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

@login_required(login_url='login')
def buscar_cep(request):
    if request.method == "POST":
        cep = request.POST.get('cep')
        if cep:

            cep_data = apiGetCep(cep).return_data_cep()
            
            if cep_data:
            
                return JsonResponse(cep_data)
        else:
            return JsonResponse({'error': 'CEP não fornecido'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)


@login_required(login_url='login')
def send_request_senior_soc_prestador(request):
    if request.method == 'POST':
        all_data = request.POST.dict()
        
        if all_data:
            
            result = send_web_service_soc(data=all_data)
            
            if result.status_code == 200:

                if isinstance(result, JsonResponse):
                    # Obtém o conteúdo JSON da resposta
                    response_json = json.loads(result.content.decode('utf-8'))
                    codigo_valor = response_json.get('codigo')  # Obtém o valor do código
                    
                    if codigo_valor:
                        
                        codigo_valor = int(codigo_valor)
                        
                        result_senior = web_service_post_prestadores(data=all_data, code_forn=codigo_valor)
                        
                        print(result_senior)
                        
                        mensagem_retorno = result_senior.mensagemRetorno  # Supondo que 'mensagemRetorno' é um atributo da classe

                        if mensagem_retorno == 'Processado com Sucesso.':
                            fornecedores = result_senior.retornosFornecedores  # Acesso à lista de fornecedores

                            for fornecedor in fornecedores:
                            
                                mensagem_retorno_fornecedor = fornecedor.retorno
                                codigo_fornecedor = fornecedor.codFor
                                
                                if mensagem_retorno_fornecedor:
                                    return JsonResponse({
                                        'message': 'Dados enviados com sucesso',
                                        'codigo': codigo_fornecedor,
                                        'retorno_senior': mensagem_retorno_fornecedor
                                    }, status=200)

                        else:
                            return JsonResponse({
                                'erro': 'Erro no processamento dos dados',
                                'mensagem': mensagem_retorno
                            }, status=400)
                    else:
                        return JsonResponse({
                            'erro': 'Código não encontrado na resposta'
                        }, status=400)
                else:
                    return JsonResponse({
                        'erro': 'Resposta não é um JsonResponse'
                    }, status=400)
            else:
                return JsonResponse({
                    'erro': f'Erro na resposta do serviço. Status code: {result.status_code}'
                }, status=result.status_code)
        
        return JsonResponse({'message': 'Nenhum dado recebido'}, status=200)

    return JsonResponse({'error': 'Método não permitido'}, status=405)

@login_required(login_url='login')
def buscar_user(request):
    if request.method == 'POST':
        login = request.POST.get('login_user')
        
        if login:
            api_user_soc = ApiUserExporta(login)
            user_dados = api_user_soc.api_user_soc()

            if user_dados and isinstance(user_dados, list):
                
                if len(user_dados) > 1:
                    return JsonResponse({'options': user_dados})

                nome_user = user_dados[0].get('nome', 'Nome não encontrado')
                codigo_user = user_dados[0].get('codigo', 'Nome não encontrado')
                return JsonResponse({'nome_user': nome_user, 'codigo_user': codigo_user})
            
            if not user_dados:
                return JsonResponse({'erro': 'nome_user não encontrado'}, status=404)


        return JsonResponse({'erro': 'nome_user não encontrado'}, status=404)

    return JsonResponse({'error': 'Método não permitido'}, status=405)