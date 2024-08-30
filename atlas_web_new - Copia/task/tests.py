from datetime import *

def teste_data_ordem(data:dict) -> list:
    
    codEmp = data.get("codigo-empresa", "codigo-empresa nao localizado")
    codFil = data.get("codigo-filial", "codigo-filial nao localizado")
    codFor = data.get("codigo_prestador", "codigo_prestador nao localizado")
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
    
    try:
        datEmi = datetime.strptime(data.get("data-emissao", "data-emissao nao localizado"), '%Y-%m-%d')
    except ValueError:
        datEmi = "data-emissao invalida"
    
    try:
        datEnt = datetime.strptime(data.get("data-pagamento", "data-pagamento nao localizado"), '%Y-%m-%d')
    except ValueError:
        datEnt = "data-pagamento invalida"

    numPrj = data.get("numero-projeto", "numero-projeto nao localizado")
    codFpj = data.get("codigo-fase-projeto", "codigo-fase-projeto nao localizado")
    codCcu = data.get("codigo-centro-custo", "codigo-centro-custo nao localizado")
    obsRat = data.get("observacao-ordem-compra", "observacao-ordem-compra nao localizado")
    ctaRed = data.get("codigo_conta_contabil", "codigo_conta_contabil nao localizado")
    
    preUni = preUni.replace(',', '.')
    vlrPar = vlrPar.replace(',', '.')
    
    list_data = [
        codEmp,
        codFil, 
        codFor, 
        ctaFin, 
        codCpg, 
        codUsu, 
        codPro, 
        preUni, 
        qtdPed, 
        vlrPar, 
        uniFor, 
        codFam, 
        codDep, 
        datEmi.strftime('%d/%m/%Y') if isinstance(datEmi, datetime) else datEmi,
        datEnt.strftime('%d/%m/%Y') if isinstance(datEnt, datetime) else datEnt, 
        numPrj, 
        codFpj, 
        codCcu, 
        obsRat, 
        ctaRed
    ]
    
    return list_data


data = {
'csrfmiddlewaretoken': '8N0Q7t2GIA2ioDBbUAMyYBFbviXWVJU5QxR6sI7A8eda7AiuMNgnMWamuzdoGRjT',
'codigo-empresa': '10',
'codigo-filial': '1001',
'cnpj-prestador': '98.781.501/0001-57',
'cnpj-cliente': '17.278.921/0001-13',
'conta-financeira': '4',
'condicao_pagamento': '03',
'codigo-usuario': '33',
'produto_senior': '804',
'valor_unitario': '2,00',
'quantidade-produto': '2',
'valor-total-produto': '4,00',
'unidade_produto': 'UN',
'cod_familia_produto': '03',
'Cod_deposito_produto_estoque': '001',
'data-emissao': '2024-08-29',
'data-pagamento': '2024-08-29',
'numero-projeto': '1',
'codigo-fase-projeto': '1592',
'codigo-centro-custo': '20',
'observacao-ordem-compra': 'teste',
'codigo_prestador': '4862',
'nome_prestador': 'TESTE - PRESTADOR - TOTALLIFE',
'codigo_cliente': '392453',
'nome_cliente': 'TESTE SUPORTE'}



print(teste_data_ordem(data=data))

