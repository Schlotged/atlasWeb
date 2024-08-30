import base64
import hashlib
import logging
from datetime import datetime, timedelta
from requests import Session
import time
import os
from django.http import JsonResponse
import re


def send_web_service_soc(data:dict):
    
    # Configuração do logging
    # logging.basicConfig(level=logging.DEBUG)
    # logger = logging.getLogger(__name__)

    def create_wsse_header(username, password):
        nonce = base64.b64encode(os.urandom(16)).decode('utf-8')  # Gerar nonce aleatório
        created_time = (datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%SZ')  # UTC no formato correto
        expires_time = (datetime.utcnow() + timedelta(minutes=5)).strftime('%Y-%m-%dT%H:%M:%SZ')  # Expiração ajustada

        sha1 = hashlib.sha1()
        sha1.update(base64.b64decode(nonce) + created_time.encode('utf-8') + password.encode('utf-8'))
        password_digest = base64.b64encode(sha1.digest()).decode('utf-8')

        wsse_ns = "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
        wsu_ns = "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

        wsse_header = f"""
        <wsse:Security xmlns:wsse="{wsse_ns}" xmlns:wsu="{wsu_ns}" soapenv:mustUnderstand="1">
            <wsu:Timestamp wsu:Id="Timestamp-{nonce}">
                <wsu:Created>{created_time}</wsu:Created>
                <wsu:Expires>{expires_time}</wsu:Expires>
            </wsu:Timestamp>
            <wsse:UsernameToken wsu:Id="UsernameToken-{nonce}">
                <wsse:Username>{username}</wsse:Username>
                <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{password_digest}</wsse:Password>
                <wsse:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{nonce}</wsse:Nonce>
                <wsu:Created>{created_time}</wsu:Created>
            </wsse:UsernameToken>
        </wsse:Security>
        """
        return wsse_header


    wsdl = 'https://ws1.soc.com.br/WSSoc/PrestadorWs'
    username = 'U2774513'
    password = '238c15958d693d2cef56211c4ba379c2f9d9ad7a'
    
    codigoUsuario = data.get('usuario-login', '')
    nome = data.get('nomePrestador', '')
    razaoSocial = data.get('razaoSocial', '')
    tipoPrestador = data.get('tipo-prestador', '')
    tipoPessoa = data.get('tipo-pessoa', '')
    uf = data.get('uf', '')
    avisoSobrePrestador = data.get('avisoSobrePrestador', '')
    representanteLegal = data.get('representanteLegal', '')
    cep = data.get('cep', '')
    endereco = data.get('endereco', '')
    numero = data.get('numeroCep', '')
    complemento = data.get('complemento', '')
    bairro = data.get('bairro', '')
    cidade = data.get('localidade', '')
    cidadeCodigoIbge = data.get('ddd', '')
    telefone = data.get('telefonePrestador', '')
    email = data.get('emailPrestador', '')
    horaInicialAtendimento = data.get('horaInicialAtendimento', '')
    horaFinalAtendimento = data.get('horaFinalAtendimento', '')
    tipoAtendimento = data.get('tipoAtendimento', '')
    comentario = data.get('comentarioPrestador', '')
    pagamentoAntecipado = data.get('pagamentoAntecipado', '')
    responsavel = data.get('responsavel', '')
    statusContrato = data.get('statusContrato', '')
    titularConta = data.get('titularConta', '')
    codigoBanco = data.get('codigoBanco', '')
    codigoAgencia = data.get('codigoAgencia', '')
    banco = data.get('banco', '')
    contaCorrente = data.get('contaCorrente', '')
    diaDoPagamento = data.get('diaDoPagamento', '')
    tipoPagamento = data.get('tipoPagamento', '')
    dataPagamento = data.get("dataPagamento", "")
    tipoDocumento = data.get('tipoDocumento', '')
    dataContratacao = data.get('dataContratacao', '')
    codigoCondicaoFaturamento = data.get('codigoCondicaoFaturamento', '')
    prestadorAtivo = data.get('prestadorAtivo', '')
    observacaogeral = data.get('observacao-geral', '')
    
    cpf = data.get('cpf', 'não foi possivel encontrar CPF')
    
    cnpj = data.get('cpf', 'não foi possivel encontrar CPF')
    
    if len(cnpj) < 18:
        cnpj = ''
    
    if len(cpf) > 11:
        cpf = ''
    
    campanha = 'N'
    ambulatorio = 'N'

    session = Session()
    soap_body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.soc.age.com/">
        <soapenv:Header>
            {create_wsse_header(username, password)}
        </soapenv:Header>
        <soapenv:Body>
            <ser:incluirPrestador>
                <IncluirPrestadorWsVo>
                    <identificacaoWsVo>
                        <codigoEmpresaPrincipal>291653</codigoEmpresaPrincipal>
                        <codigoResponsavel>105824</codigoResponsavel>
                        <codigoUsuario>{codigoUsuario}</codigoUsuario>
                    </identificacaoWsVo>
                    <dadosPrestadorWsVo>
                        <tipoPrestador>{tipoPrestador}</tipoPrestador>
                        <tipoPessoa>{tipoPessoa}</tipoPessoa>
                        <nome>{nome}</nome>
                        <razaoSocial>{razaoSocial}</razaoSocial>
                        <responsavel>{responsavel}</responsavel>
                        <conselhoClasse></conselhoClasse>
                        <uf>{uf}</uf>
                        <especialidadeResponsavel1></especialidadeResponsavel1>
                        <especialidadeResponsavel2></especialidadeResponsavel2>
                        <nivelClassificacao>PREFERENCIAL</nivelClassificacao>
                        <avisoSobrePrestador>{avisoSobrePrestador}</avisoSobrePrestador>
                        <representanteLegal>{representanteLegal}</representanteLegal>
                        <prestadorLocalidadeWsVo>
                            <cep>{cep}</cep>
                            <endereco>{endereco}</endereco>
                            <numero>{numero}</numero>
                            <complemento>{complemento}</complemento>
                            <bairro>{bairro}</bairro>
                            <cidade>{cidade}</cidade>
                            <cidadeCodigoIbge>{cidadeCodigoIbge}</cidadeCodigoIbge>
                            <uf>{uf}</uf>
                            <atendente></atendente>
                            <telefone>{telefone}</telefone>
                            <telefoneCelular></telefoneCelular>
                            <fax></fax>
                            <email>{email}</email>
                        </prestadorLocalidadeWsVo>
                        <prestadorAtendimentoWsVo>
                            <horaInicialAtendimento>{horaInicialAtendimento}</horaInicialAtendimento>
                            <horaFinalAtendimento>{horaFinalAtendimento}</horaFinalAtendimento>
                            <tipoAtendimento>{tipoAtendimento}</tipoAtendimento>
                            <exibirInformacaoPedidoExame>Sim</exibirInformacaoPedidoExame>
                            <comentario>{comentario}</comentario>
                            <pagamentoAntecipado>{pagamentoAntecipado}</pagamentoAntecipado>
                            <ambulatorio>{ambulatorio}</ambulatorio>
                            <campanha>{campanha}</campanha>
                        </prestadorAtendimentoWsVo>
                        <prestadorContratoWsVo>
                            <ativo>{prestadorAtivo}</ativo>
                            <esporadico>Não</esporadico>
                            <dataContratacao>{dataContratacao}</dataContratacao>
                            <dataCancelamento></dataCancelamento>
                            <motivoCancelamento></motivoCancelamento>
                            <statusContrato>{statusContrato}</statusContrato>
                        </prestadorContratoWsVo>
                        <prestadorInformacaoBancariaWsVo>
                            <titularConta>{titularConta}</titularConta>
                            <cpf>{cpf}</cpf>
                            <cnpj>{cnpj}</cnpj>
                            <codigoBanco>{codigoBanco}</codigoBanco>
                            <codigoAgencia>{codigoAgencia}</codigoAgencia>
                            <banco>{banco}</banco>
                            <contaCorrente>{contaCorrente}</contaCorrente>
                        </prestadorInformacaoBancariaWsVo>
                        <prestadorDadosPagamentoWsVo>
                            <diaDoPagamento>{diaDoPagamento}</diaDoPagamento>
                            <prestadorPadrao>Sim</prestadorPadrao>
                            <condicaoFaturamento>{codigoCondicaoFaturamento}</condicaoFaturamento>
                            <tipoPagamento>{tipoPagamento}</tipoPagamento>
                            <dataPagamento>{dataPagamento}</dataPagamento>
                            <tipoDocumento>{tipoDocumento}</tipoDocumento>
                        </prestadorDadosPagamentoWsVo>
                        <prestadorDadoComplementarWsVo>
                            <cabecalho></cabecalho>
                            <rodape></rodape>
                            <observacao>{observacaogeral}</observacao>
                            <textoLivre></textoLivre>
                        </prestadorDadoComplementarWsVo>
                    </dadosPrestadorWsVo>
                </IncluirPrestadorWsVo>
            </ser:incluirPrestador>
        </soapenv:Body>
    </soapenv:Envelope>
    """


    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': '""'  # SOAPAction pode ser vazio se não especificado
    }

    # print(create_wsse_header(username, password))

    response = session.post(wsdl, data=soap_body, headers=headers)
    

    # logger.debug(f"Status Code: {response.status_code}")
    # logger.debug(f"Response Text: {response.text}")

    if response.status_code == 200:
        # logger.info(f"Response Text: {response.text}")
        try:
            match = re.search(r'<codigo>(\d+)</codigo>', response.text)

            if match:
                codigo_valor = match.group(1)
                return JsonResponse({
                    'message': 'Cadastrado com sucesso', 
                    'codigo': codigo_valor
                }, status=200)
            else:
                return JsonResponse({
                    'erro': 'Cadastro com dados inválidos'
                }, status=400)
        except:
            
            return JsonResponse({
                    'erro': 'Cadastro com dados inválidos'
                }, status=400)
        
        
    else:
        
        # logger.error(f"Falha na requisição SOAP: {response.status_code} - {response.text}")
        return JsonResponse({
                    'erro': 'Cadastro com dados inválidos'
                }, status=400)
