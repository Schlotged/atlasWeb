import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


class ApiPrestadorExportaDados:
    def __init__(self, cnpj_company: str):
        super().__init__()
        
        self.cnpj_prestador_input = str(cnpj_company)

    def api_prestador_soc(self):
        
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
            # print("Dados recebidos com sucesso!")
            # print(response.text)  # Imprime o conteúdo da resposta

            if tiposaida == 'json':
                dados_json = json.loads(response.text)

                if isinstance(dados_json, list):
                    status = True
                    for item in dados_json:
                        try:

                            cnpj_prestador = item.get("cnpj", "cnpj Não Encontrado")
                            
                            if self.cnpj_prestador_input == str(cnpj_prestador):
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
                
                print(lista_prestadores)
                
                return lista_prestadores

        else:
            print("Erro ao receber dados. Status code:", response.status_code)