
import requests
import json

class ApiUserExporta:
    def __init__(self, var_exame: str):
        super().__init__()
        self.users = var_exame
    
    def api_user_soc(self):
        empresa = "291653"
        codigo = "186476"
        chave = "c06ef1ba162f1fe3f468"
        tiposaida = "json"
        usuario = f'{self.users}'
        status = '1'
        
        lista_user = []

        url = "https://ws1.soc.com.br/WebSoc/exportadados"

        parametros = {
            "empresa":empresa,
            "codigo":codigo,
            "chave":chave,
            "tipoSaida":tiposaida,
            "ativo":status
            }


        url_completa = url + "?parametro=" + str(parametros)

        response = requests.get(url_completa)

        if response.status_code == 200:
            # print("Dados recebidos com sucesso!")
            # print(response.text)  # Imprime o conteúdo da resposta

            if tiposaida == 'json':
                dados_json = json.loads(response.text)

                if isinstance(dados_json, list):
                    status = False
                    for item in dados_json:
                        try:
                            login_user = item.get("LOGIN_USUARIO", "LOGIN_USUARIO Não Encontrado")
                            codigo = item.get("CD_USUARIO", "CODIGO Não Encontrado")
                            
                            if login_user == usuario:

                                status = True

                                lista_user.append({
                                    "nome": login_user,
                                    "codigo": codigo,
                                })

                        except:
                            print(f"Nome Abreviado: Erro na leitura")
                        
                else:
                    print("Dados JSON não são uma lista")
            
            if status:
                return lista_user
            
            else:
                
                return {
                    'erro': 'Usuario não localizado'
                }

        else:
            print("Erro ao receber dados. Status code:", response.status_code)
