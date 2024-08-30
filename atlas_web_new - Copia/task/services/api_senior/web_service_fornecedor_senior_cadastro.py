import logging
from zeep import Client, Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from requests import Session

# def web_service_get_prestadores(codfor):

#     # logging.basicConfig(level=logging.INFO)
#     # logging.getLogger('zeep.transports').setLevel(logging.DEBUG)

#     wsdl_url = "https://webp07.seniorcloud.com.br:30511/g5-senior-services/sapiens_Synccom_senior_g5_co_cad_fornecedor?wsdl"

#     session = Session()
#     transport = Transport(session=session)

#     history = HistoryPlugin()

#     client = Client(wsdl=wsdl_url, transport=transport, plugins=[history])

#     usuario = "gedson.silva"
#     senha = "Ttl@#2141g"

#     try:
#         response = client.service.Exportar(
#             user=usuario,
#             password=senha,
#             encryption=0,
#             parameters={
#                 'codEmp': 10,
#                 'codFor': codfor,
#                 'sitFor': '',
#                 'filtroFornecedores': {'codFor': codfor},
#                 'codFil': 1001,
#                 'identificadorSistema': 'TL',
#                 'quantidadeRegistros':1,
#                 'tipoIntegracao':'T'
#             }
#         )

#         return response

#     except Fault as e:

#         print(f'Error: {e}')


def web_service_post_prestadores(data:dict, code_forn:int):
    
    # logging.basicConfig(level=logging.INFO)
    # logging.getLogger('zeep.transports').setLevel(logging.DEBUG)
    
    wsdl_url = "https://webp07.seniorcloud.com.br:30511/g5-senior-services/sapiens_Synccom_senior_g5_co_ger_cad_fornecedores?wsdl"

    session = Session()
    transport = Transport(session=session)

    history = HistoryPlugin()

    client = Client(wsdl=wsdl_url, transport=transport, plugins=[history])

    usuario = "gedson.silva"
    senha = "Ttl@#2141g"

    nome = data.get('nomePrestador', '')
    razaoSocial = data.get('razaoSocial', '')
    tipFor = data.get('tipo-pessoa', '')
    uf = data.get('uf', '')
    cep = data.get('cep', '')
    endereco = data.get('endereco', '')
    bairro = data.get('bairro', '')
    cidade = data.get('localidade', '')
    telefone = data.get('telefonePrestador', '')
    email = data.get('emailPrestador', '')
    cpf = data.get('cpf', '')
    condicaoPagamento = data.get('condicaoPagamento', '')
    nenFor = data.get('numeroCep', '')
    cplEnd = data.get('complemento', '')

    cpf = cpf.replace('.', '').replace('/', '').replace('-', '')

    if tipFor == "JURIDICA":
        tipFor = 'J'
    
    elif tipFor == "FISICA":
        tipFor = 'F'
    
    
    try:
        response = client.service.GravarFornecedores_7(
            user=usuario,
            password=senha,
            encryption=0,
            parameters={
                "dadosGeraisFornecedor": {
                    "codFor": code_forn,
                    "nomFor": razaoSocial,
                    "apeFor": nome,
                    "tipFor": tipFor,
                    "tipEmp": 0,
                    "tipMer": "I",
                    "insEst": "",
                    "insMun": "",
                    "cgcCpf": cpf,
                    "codSuf": "",
                    "endFor": endereco,
                    "cplEnd": cplEnd,
                    "baiFor": bairro,
                    "zipCod": "",
                    "cepFor": int(cep),
                    "cepIni": 0,
                    "cidFor": cidade,
                    "sigUfs": uf,
                    "fonFor": telefone,
                    "fonFo2": "",
                    "fonFo3": "",
                    "faxFor": "",
                    "cxaPst": 0,
                    "intNet": email,
                    "nomVen": "",
                    "fonVen": "",
                    "rmlVen": 0,
                    "faxVen": "",
                    "codIac": 0,
                    "abrIac": "",
                    "indBsp": "N",
                    "sitFor": "A",
                    "codPai": "",
                    "gerDir": "",
                    "ideFor": "",
                    "qtdDep": 0,
                    "recPis": "N",
                    "perPid": "",
                    "triIss": "N",
                    "recCof": "N",
                    "perCod": "N",
                    "retCof": "N",
                    "retCsl": "N",
                    "retPis": "N",
                    "retOur": "N",
                    "recIpi": "N",
                    "recIcm": "N",
                    "triIcm": "N",
                    "triIpi": "N",
                    "retPro": "",
                    "retIrf": "",
                    "indFor": "P",
                    "limRet": "E",
                    "numRge": "",
                    "perRir": "",
                    "perRin": "",
                    "nenFor": nenFor,
                    "definicoesFornecedor": {
                        "codEmp": 10,
                        "codFil": 1001,
                        "codTpr": "",
                        "codCpg": condicaoPagamento,
                        "codFpg": 0,
                        "codTra": 0,
                        "codPor": "",
                        "codCrt": "",
                        "pagJmm": "",
                        "pagDtj": 0,
                        "pagMul": "",
                        "pagDtm": 0,
                        "perDsc": "",
                        "tolDsc": 0,
                        "antDsc": "N",
                        "perDs1": "",
                        "perDs2": "",
                        "perDs3": "",
                        "perDs4": "",
                        "perDs5": "",
                        "perFun": "",
                        "perIns": "",
                        "indInd": "N",
                        "perFre": "",
                        "perSeg": "",
                        "perEmb": "",
                        "perEnc": "",
                        "perOut": "",
                        "perIss": "",
                        "perIrf": "",
                        "cifFob": "",
                        "perIne": "",
                        "ctaRed": 0,
                        "ctaAux": 0,
                        "ctaAad": 0,
                        "przEnt": 0,
                        "qtdDcv": 0,
                        "criEdv": "",
                        "codBan": "",
                        "tipTcc": 0,
                        "codAge": "",
                        "ccbFor": "",
                        "codCrp": "",
                        "pagTir": "",
                        "ctaRcr": 0,
                        "ctaFdv": 0,
                        "ctaFcr": 0,
                        "seqOrm": 0,
                        "codFav": 0.0,
                        "rvlCfr": "",
                        "rvlFre": "",
                        "rvlSeg": "",
                        "rvlEmb": "",
                        "rvlEnc": "",
                        "rvlOut": "",
                        "rvlDar": "",
                        "rvlFei": "",
                        "rvlSei": "",
                        "rvlOui": "",
                        "codDep": "",
                        "forMon": "N",
                        "pgtMon": "N",
                        "pgtFre": "OC",
                        "tnsPro": "",
                        "tnsSer": "",
                        "codEdc": "",
                        "cqdCvn": "",
                        "perSen": "N",
                        "perGil": "N",
                        "defCamposUsuario": { "campo": "", "valor": usuario }
                    },
                    "codCli": 10,
                    "marFor": "",
                    "codRam": "",
                    "codGre": 0,
                    "forRep": 0,
                    "forTra": 0,
                    "notSis": 0,
                    "notFor": 0,
                    "codTri": "",
                    "cliFor": "",
                    "codRoe": "",
                    "seqRoe": 0,
                    "codSro": "",
                    "eenFor": "",
                    "forWms": "",
                    "emaNfe": "",
                    "codMot": 0,
                    "obsMot": "",
                    "temOrm": "",
                    "notAfo": 0,
                    "insAnp": 0,
                    "indCoo": "",
                    "codRtr": 0,
                    "regEst": 0,
                    "tipPgt": "",
                    "perIcm": 0,
                    "numIdf": "",
                    "tipEmc": "",
                    "entPaa": "",
                    "orgEmi": "",
                    "datExd": "",
                    "datNas": "",
                    "numCbo": 0,
                    "catFor": 0,
                    "tipAce": 0,
                    "numNis": "",
                    "ideExt": "",
                    "forApo": "",
                    "cpfMei": 0.0,
                    "indFtr": 0,
                    "codCae": 0.0,
                    "cadastroCEP": {
                        "cepIni": "",
                        "cepFim": "",
                        "codRai": 0,
                        "nomCid": "",
                        "baiCid": "",
                        "endCid": "",
                        "cepPol": ""
                    },
                    "indFti": 0,
                    "isiFor": 0,
                    "renAse": "",
                    "cadastroPIX": {
                        "codEmp": 10,
                        "codFil": 1001,
                        "seqChv": "",
                        "tpcPix": 2,
                        "chvPix": "teste@gmail.com",
                        "chvPdr": "S"
                    },
                    "parametrosDinamicos": { "chave": "", "valor": "" },
                    "datICP": "",
                    "datFCP": "",
                    "dadosGeraisCamposUsuario": { "campo": '', "valor": usuario },
                    "codHas": "",
                    },
                    "sistemaIntegracao": "TL",
                    "dataBuild": ""
            }
        )  
        
        logging.info(f'Resposta: {response}')

        return response

    except Fault as e:

        print(f'Error: {e}')


# web_service_post_prestadores()