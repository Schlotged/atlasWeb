import logging
from zeep import Client, Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from requests import Session


logging.basicConfig(level=logging.INFO)
logging.getLogger('zeep.transports').setLevel(logging.DEBUG)


wsdl_url = "https://webp07.seniorcloud.com.br:30511/g5-senior-services/sapiens_Synccom_senior_g5_co.mcm_cpr_ordemcompra?wsdl"


session = Session()
transport = Transport(session=session)

history = HistoryPlugin()

client = Client(wsdl=wsdl_url, transport=transport, plugins=[history])

usuario = "gedson.silva"
senha = "Ttl@#2141g"

try:
    response = client.service.ConsultarGeral(
        user=usuario,
        password=senha,
        encryption=0,
        parameters={
            'codEmp': 10,
            'codFor': {'codFor': '5542'},
            'codFil': 1001,
            'numOcp': {'numOcp': 4},
            'identificadorSistema': 'TL',
            'codTra': {'codTra': 0},
            'indicePagina': 1,
            'datEmiIni': '20/08/2024',
            'limitePagina': 1,
            'sitOcp': {'sitOcp': 4},
            'datEmiFim': '20/08/2024' 
        }
    )

    print(response)

except Fault as e:

    print(f'Error: {e}')
