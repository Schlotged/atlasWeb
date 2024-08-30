from zeep import Client
from zeep.exceptions import Fault

# URL do WSDL
wsdl_url = "https://webp07.seniorcloud.com.br:30511/g5-senior-services/sapiens_Synccom_senior_g5_co_mcm_cpr_ordemcompra?wsdl"

# Cliente SOAP
client = Client(wsdl=wsdl_url)

# Credenciais
usuario = "gedson.silva"
senha = "Ttl@#2141g"

# Parâmetros ajustados
try:
    response = client.service.Exportar(
        user=usuario,
        password=senha,
        encryption=0,
        parameters={
            'codEmp': 10,
            'numOcp': '4',
            'codFil': 1001,
            'identificadorSistema': 'TL',
            'quantidadeRegistros': 1,
            'tipoIntegracao': 'T'
        }
    )
    # Exibir a resposta
    print(response)
    
    
except Fault as e:
    print(f'Error: {e}')
