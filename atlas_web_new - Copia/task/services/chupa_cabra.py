
import os
from dotenv import load_dotenv
import requests
import json
import logging
from zeep import Client, Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from requests import Session
from tqdm import tqdm

load_dotenv()


class chupaCabra:
    
    def __init__(self):
        pass
    
    def api_soc_get_prestadores(self) -> list:
        
        empresa = os.getenv('API_COMPANY')
        codigo = os.getenv('API_CODE')
        chave = os.getenv('API_KEY_SOC')
        tiposaida = "json"
        
        lista_prestadores = []

        url = "https://ws1.soc.com.br/WebSoc/exportadados"

        parametros = {
            "empresa": empresa,
            "codigo": codigo,
            "chave": chave,
            "tipoSaida": tiposaida,
            "cnpj":"",
            "cpf":"",
            "cod":"",
            "ativo":"",
            "cidade":"",
            "estado":"",
            "tipoPrestador":"",
            "tipoPessoa":""
                    }
        
        url_completa = url + "?parametro=" + str(parametros)

        response = requests.get(url_completa)

        if response.status_code == 200:

            if tiposaida == 'json':
                dados_json = json.loads(response.text)

                if isinstance(dados_json, list):
                    status = True
                    for item in dados_json:
                        try:

                            cnpj_prestador = item.get("cnpj", "cnpj Não Encontrado")
                            nome_prestador = item.get("nomePrestador", "nomePrestador Não Encontrado")
                            codigo_prestador = item.get("codigoPrestador", "codigoPrestador Não Encontrado")
                            
                            status = True
                            
                            lista_prestadores.append({
                                "nome": nome_prestador,
                                "codigo": codigo_prestador,
                                "cnpj": cnpj_prestador
                            })

                        except:
                            print(f"Nome Abreviado: Erro na leitura")
                        
                else:
                    print("Dados JSON não são uma lista")
            
            if status:

                return lista_prestadores

        else:
            print("Erro ao receber dados. Status code:", response.status_code)
    
    def web_service_get_prestadores(self, codfor):

        # logging.basicConfig(level=logging.INFO)
        # logging.getLogger('zeep.transports').setLevel(logging.DEBUG)

        wsdl_url = "https://webp07.seniorcloud.com.br:30511/g5-senior-services/sapiens_Synccom_senior_g5_co_cad_fornecedor?wsdl"

        session = Session()
        transport = Transport(session=session)

        history = HistoryPlugin()

        client = Client(wsdl=wsdl_url, transport=transport, plugins=[history])

        usuario = os.getenv('USER_SENIOR')
        senha = os.getenv('PASSWORD_SENIOR')

        try:
            response = client.service.Exportar(
                user=usuario,
                password=senha,
                encryption=0,
                parameters={
                    'codEmp': 10,
                    'codFor': codfor,
                    'sitFor': '',
                    'filtroFornecedores': {'codFor': codfor},
                    'codFil': 1001,
                    'identificadorSistema': 'TL',
                    'quantidadeRegistros':1,
                    'tipoIntegracao':'T'
                }
            )

            return response

        except Fault as e:

            print(f'Error: {e}')

    def automatic_validation(self):
        
        list_codigo_prestadores_soc = []
        
        lista_prestadores_soc = self.api_soc_get_prestadores()
        
        for i in lista_prestadores_soc:
            
            codigo_prestador = i.get("codigo", "codigoPrestador Não Encontrado")
            nome_prestador = i.get("nome", "codigoPrestador Não Encontrado")

            list_codigo_prestadores_soc.append({'codigo_prestador':codigo_prestador, 'nome_prestador':nome_prestador})

        for item in list_codigo_prestadores_soc:
            
            name = item.get('nome_prestador', 'Nome não encontrado')
            code = item.get('codigo_prestador', 'codigo_prestador não encontrado')
            
            result = self.web_service_get_prestadores(code)

            try:
                # Acessa a lista de fornecedores
                fornecedores = result.fornecedor
                
                if fornecedores:
                    
                    # Itera sobre cada fornecedor
                    for fornecedor in fornecedores:
                        name_fornecedor = fornecedor.apeFor
                        
                        if name_fornecedor:
                            
                            if name == name_fornecedor:
                                print()
                                print(f'prestador: {name} encontrado')
                            else:
                                print()
                                print(f'prestador: {name} não localizado')
                        
                        else:
                            print()
                            print('Campo apeFor vazio')
                else:
                    print(f'error: retorno webservice sem json fornecedor')
            except:
                print()
                print(f'error: retorno webservice sem json fornecedor')
        


class_chupa_cabra = chupaCabra()

class_chupa_cabra.automatic_validation()