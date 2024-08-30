import requests
import json


class apiGetCep:
    
    def __init__(self, cep: int):
        
        self.cep_number = cep
    
    def return_data_cep(self) -> json:
        
        response = requests.get(f'https://viacep.com.br/ws/{self.cep_number}/json/')
        
        if response.status_code == 200:
            
            dados_json = response.json()
            
            print(dados_json)
            
            return dados_json


