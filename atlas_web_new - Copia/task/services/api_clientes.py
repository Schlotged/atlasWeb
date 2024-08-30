import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


class ApiClienteExportaDados:
    def __init__(self, cnpj_company: str):
        super().__init__()
        
        self.cnpj_prestador_input = str(cnpj_company)

    def api_prestador_soc(self):
        
        empresa = os.getenv('API_COMPANY')
        codigo = os.getenv('API_CODE_CLIENT')
        chave = os.getenv('API_KEY_SOC_CLIENT')
        tiposaida = "json"
        
        lista_clientes = []

        url = "https://ws1.soc.com.br/WebSoc/exportadados"


        parametros = {
            'empresa': empresa,
            'codigo': codigo,
            'chave': chave,
            'tipoSaida': tiposaida
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

                            cnpj_cliente = item.get("CNPJ", "cnpj Não Encontrado")
                            
                            if self.cnpj_prestador_input == str(cnpj_cliente):
                                nome_cliente = item.get("NOMEABREVIADO", "Nome Abreviado Não Encontrado")
                                codigo_cliente = item.get("CODIGO", "CODIGO Não Encontrado")
                                
                                status = True
                                
                                lista_clientes.append({
                                    "nome": nome_cliente,
                                    "codigo": codigo_cliente,
                                    "cnpj": cnpj_cliente
                                })

                        except:
                            print(f"Nome Abreviado: Erro na leitura")
                        
                else:
                    print("Dados JSON não são uma lista")
            
            if status:
                
                print(lista_clientes)
                
                return lista_clientes

        else:
            print("Erro ao receber dados. Status code:", response.status_code)


# api_soc = ApiClienteExportaDados('17.278.921/0001-13')

# api_soc.api_prestador_soc()