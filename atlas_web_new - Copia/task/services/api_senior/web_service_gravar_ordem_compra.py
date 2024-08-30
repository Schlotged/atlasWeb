import logging
from zeep import Client, Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from requests import Session
from dotenv import load_dotenv
import os

load_dotenv()


def ws_senior_ordem_compra(data:dict):

    # Configuração do logging
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('zeep.transports').setLevel(logging.DEBUG)

    # URL do WSDL
    wsdl_url = "https://webp07.seniorcloud.com.br:30511/g5-senior-services/sapiens_Synccom_senior_g5_co.mcm_cpr_ordemcompra?wsdl"

    # Configuração do transporte e cliente
    session = Session()
    transport = Transport(session=session)
    history = HistoryPlugin()
    client = Client(wsdl=wsdl_url, transport=transport, plugins=[history])

    # Credenciais de acesso
    usuario = os.getenv('USER_SENIOR')
    senha = os.getenv('PASSWORD_SENIOR')
    
    codEmp = data.get("codigo-empresa", "codigo-empresa nao localizado")
    codFil = data.get("codigo-filial", "codigo-filial nao localizado")
    codFor = data.get("codigo_prestador", "codigo_prestador nao localizado")
    data.get("codigo_cliente", "codigo_cliente nao localizado")
    ctaFin = data.get("conta-financeira", "conta-financeira nao localizado")
    codCpg = data.get("condicao_pagamento", "condicao_pagamento nao localizado")
    codUsu = data.get("codigo-usuario", "codigo-usuario nao localizado")
    codPro = data.get("produto_senior", "produto_senior nao localizado")
    preUni = data.get("valor_unitario", "valor_unitario nao localizado")
    qtdPed = data.get("quantidade-produto", "quantidade-produto nao localizado")
    vlrPar = data.get("valor-total-produto", "valor-total-produto nao localizado")
    uniFor = data.get("unidade_produto", "unidade_produto nao localizado")
    codFam = data.get("cod_familia_produto", "cod_familia_produto nao localizado")
    codDep = data.get("Cod_deposito_produto_estoque", "Cod_deposito_produto_estoque nao localizado")
    datEmi = data.get("data-emissao", "data-emissao nao localizado")
    datEnt = data.get("data-pagamento", "data-pagamento nao localizado")
    numPrj = data.get("numero-projeto", "numero-projeto nao localizado")
    codFpj = data.get("codigo-fase-projeto", "codigo-fase-projeto nao localizado")
    codCcu = data.get("codigo-centro-custo", "codigo-centro-custo nao localizado")
    obsRat = data.get("observacao-ordem-compra", "observacao-ordem-compra nao localizado")
    ctaRed = data.get("codigo_conta_contabil", "codigo_conta_contabil nao localizado")

    diaPar = 30


    try:
        response = client.service.GravarOrdensCompra_6(
            user=usuario,
            password=senha,
            encryption=0,
            parameters = {
                
                "dadosGerais": {
                    "codEmp": 20,
                    "codFil": 2001,
                    "numOcp": 0,
                    "tnsPro": "90400",
                    "tnsSer": "",
                    "datEmi": "28/08/2024",
                    "codFor": 1,
                    "codCpg": "03",
                    "codTra": 0,
                    "vlrFre": 0.0,
                    "somFre": "N",
                    "vlrSeg": 0.00,
                    "vlrEmb": 0.0,
                    "vlrEnc": 0.0,
                    "vlrOut": 0.0,
                    "vlrDar": 0.0,
                    "vlrFrd": 0.0,
                    "vlrOud": 0.0,
                    "vlrDs1": 0.0,
                    "vlrDs2": 0.0,
                    "vlrDzf": 0.0,
                    "vlrBfu": 0.0,
                    "vlrBse": 0.0,
                    "vlrFun": 0.0,
                    "vlrBsp": 0.0,
                    "vlrStp": 0.0,
                    "vlrBsc": 0.0,
                    "vlrStc": 0.0,
                    "vlrBin": 0.0,
                    "vlrIns": 0.0,
                    "vlrLpr": 0.0,
                    "vlrLse": 0.0,
                    "vlrLou": 0.0,
                    "vlrLiq": 0.0,
                    "vlrFin": 0.0,
                    "temPar": 0.0,
                    "seqOrm": 0,
                    "vlrDs3": 0.0,
                    "vlrDs4": 0.0,
                    "salCan": "",
                    "perDs1": 0.0,
                    "perDs2": 0.0,
                    "perDs3": 0.0,
                    "perDs4": 0.0,
                    "perDs5": 0.0,
                    "produtos": {
                        "seqIpo": 1,
                        "tnsPro": "90400",
                        "codPro": "846",
                        "codDer": "",
                        "cplIpo": "",
                        "uniFor": "UN",
                        "codFam": "03",
                        "codDep": "001",
                        "qtdPed": 80.0,
                        "uniMed": "UN",
                        "qtdFor": 0.0,
                        "codTpr": "",
                        "preUni": 10.0,
                        "preFix": "N",
                        "perDsc": 0.0,
                        "perIpi": 0.0,
                        "perIcm": 0.0,
                        "codTst": "",
                        "vlrBsi": 0.00,
                        "vlrIcs": 0.0,
                        "datEnt": "28/08/2024",
                        "numPrj": 1,
                        "codFpj": 2200,
                        "ctaFin": 680,
                        "ctaRed": 1592,
                        "codCcu": "20",
                        "vlrFre": 0.0,
                        "vlrSeg": 0.0,
                        "vlrEmb": 0.0,
                        "vlrEnc": 0.0,
                        "vlrOut": 0.0,
                        "vlrDar": 0.0,
                        "vlrDsc": 0.0,
                        "codMoe": "01",
                        "datMoe": "",
                        "cotMoe": 0.0,
                        "fecMoe": "",
                        "perIim": 0.0,
                        "perIrf": 0.0,
                        "perIci": 0.0,
                        "preFor": 0.0,
                        "perDs1": 0.0,
                        "perDs2": 0.0,
                        "perDs3": 0.0,
                        "perDs4": 0.0,
                        "perDs5": 0.0,
                        "aliFcp": 0.00,
                        "astFcp": 0.0,
                        "areFcp": 0.00,
                        "loteSerie": {
                            "seqDls": 0,
                            "codDep": "001",
                            "datEnt": "28/08/2024",
                            "datVlt": "28/08/2024",
                            "codLot": "",
                            "numSep": "",
                            "qtdEst": 0.0,
                            "obsDls": "",
                            "vlrDm1": 0.0,
                            "vlrDm2": 0.0,
                            "vlrDm3": 0.0,
                            "vlrDm4": 0.0,
                            "vlrDm5": 0.0,
                            "vlrDm6": 0.0,
                            "datFab": "28/08/2024"
                        },
                        "rateioProduto": {
                            "numPrj": 1,
                            "codFpj": 2200,
                            "ctaFin": 680,
                            "ctaRed": 1592,
                            "perCta": 100.0,
                            "vlrCta": 0.0,
                            "codCcu": "20",
                            "perRat": 100.0,
                            "vlrRat": 0.0,
                            "obsRat": "produto interno"
                        },
                        "camposUsuarioItemProduto": {
                            "cmpUsu": usuario,
                            "vlrUsu": ''
                        },
                    },
                    "pedFor": "",
                    "parcelas": {
                        "seqPar": 0,
                        "codCrp": "",
                        "codFcr": "",
                        "datFcr": "",
                        "diaPar": 30,
                        "vctPar": "",
                        "perPar": 100.0,
                        "vlrPar": 800.0,
                        "dscPar": 0.0,
                        "obsPar": "",
                        "indPag": ""
                    },
                    "observacoes": {
                        "seqObs": 0,
                        "tipObs": "",
                        "codMot": 0,
                        "obsOcp": ""
                    },
                    "camposUsuarioDadosGerais": { 
                        "cmpUsu": usuario, 
                        "vlrUsu": "" 
                    },
                    "cifFob": "",
                    "codUsu": 33.0,
                    "ideExt": 0,
                    "tipoProcessamento": 1,
                    "fechaOC": 0,
                    "obsOcp": "",
                    "codMot": "",
                    "obsMot": "",
                    "prcOcp": 0,
                    "codMoe": "",
                    "codFpg": 2,
                    "excluirItens": ""
                },
                "tipoProcessamento": "1",
                "fechaOC": "",
                "identificadorSistema": "TL"
            }
        )
        
        logging.info(f'Resposta da API: {response}')
        
        return response
        
    except Fault as fault:
        logging.error(f'Ocorreu um erro na chamada SOAP: {fault}')
    except Exception as e:
        logging.error(f'Ocorreu um erro inesperado: {e}')


ws_senior_ordem_compra()