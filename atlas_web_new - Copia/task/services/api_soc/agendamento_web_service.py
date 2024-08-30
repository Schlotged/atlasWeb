import base64
import hashlib
import logging
from datetime import datetime, timedelta
from requests import Session
import time
import os

# Configuração do logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_wsse_header(username, password):
    nonce = base64.b64encode(os.urandom(16)).decode('utf-8')  # Gerar nonce aleatório
    created_time = (datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%SZ')  # UTC no formato correto
    expires_time = (datetime.utcnow() + timedelta(minutes=5)).strftime('%Y-%m-%dT%H:%M:%SZ')  # Expiração ajustada

    sha1 = hashlib.sha1()
    sha1.update(base64.b64decode(nonce) + created_time.encode('utf-8') + password.encode('utf-8'))
    password_digest = base64.b64encode(sha1.digest()).decode('utf-8')

    wsse_ns = "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
    wsu_ns = "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

    wsse_header = f"""
    <wsse:Security xmlns:wsse="{wsse_ns}" xmlns:wsu="{wsu_ns}" soapenv:mustUnderstand="1">
        <wsu:Timestamp wsu:Id="Timestamp-{nonce}">
            <wsu:Created>{created_time}</wsu:Created>
            <wsu:Expires>{expires_time}</wsu:Expires>
        </wsu:Timestamp>
        <wsse:UsernameToken wsu:Id="UsernameToken-{nonce}">
            <wsse:Username>{username}</wsse:Username>
            <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{password_digest}</wsse:Password>
            <wsse:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{nonce}</wsse:Nonce>
            <wsu:Created>{created_time}</wsu:Created>
        </wsse:UsernameToken>
    </wsse:Security>
    """
    return wsse_header

# Dados da requisição
username = 'U2934059'
password = '5fbb11dad5fe9bbdbef7810487793a2cfd8c90a6'
wsdl = 'https://ws1.soc.com.br/WSSoc/AgendamentoWs'

# Criar cliente e enviar a requisição
session = Session()
soap_body = f"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.soc.age.com/">
    <soapenv:Header>
        {create_wsse_header(username, password)}
    </soapenv:Header>
    <soapenv:Body>
        <ser:incluirAgendamento>
            <IncluirAgendamentoWsVo>
                <identificacaoWsVo>
                    <codigoEmpresaPrincipal>291653</codigoEmpresaPrincipal>
                    <codigoResponsavel>105824</codigoResponsavel>
                    <codigoUsuario>1576172</codigoUsuario>
                </identificacaoWsVo>
                <dadosAgendamentoWsVo>
                    <tipoBuscaEmpresa>CODIGO_SOC</tipoBuscaEmpresa>
                    <codigoEmpresa>1222199</codigoEmpresa>
                    <tipoBuscaFuncionario>CODIGO_SOC</tipoBuscaFuncionario>
                    <codigoFuncionario>0000000001</codigoFuncionario>
                    <codigoUsuarioAgenda>2558572</codigoUsuarioAgenda>
                    <data>28/08/2024</data>
                    <horaInicial>18:00</horaInicial>
                    <codigoCompromisso>13</codigoCompromisso>
                    <usaOutroCompromisso>N</usaOutroCompromisso>
                    <tipoCompromisso>PERIODICO</tipoCompromisso>
                    <detalhes>Consulta agendada</detalhes>
                    <codigoProfissionalAgenda></codigoProfissionalAgenda>
                    <horarioChegada>08:50</horarioChegada>
                    <horarioSaida></horarioSaida>
                    <priorizarAtendimento>N</priorizarAtendimento>
                    <atendido>N</atendido>
                    <usaEnviarEmail>False</usaEnviarEmail>
                    <emailWsVo>
                        <data>21/08/2024</data>
                        <hora>09:00</hora>
                        <email>joao.silva@example.com</email>
                    </emailWsVo>
                    <usaEnviarSocms>N</usaEnviarSocms>
                    <socmsWsVo>
                        <data></data>
                        <hora></hora>
                        <telefone></telefone>
                        <codigoMensagem></codigoMensagem>
                        <mensagem></mensagem>
                    </socmsWsVo>
                    <codigoPrestador>4862</codigoPrestador>
                </dadosAgendamentoWsVo>
            </IncluirAgendamentoWsVo>
        </ser:incluirAgendamento>
    </soapenv:Body>
</soapenv:Envelope>
"""


headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': '""'  # SOAPAction pode ser vazio se não especificado
}

response = session.post(wsdl, data=soap_body, headers=headers)

logger.debug(f"Status Code: {response.status_code}")
logger.debug(f"Response Text: {response.text}")

# Verificar resposta e possíveis erros
if response.status_code == 200:
    logger.info("Requisição SOAP enviada com sucesso.")
else:
    logger.error(f"Falha na requisição SOAP: {response.status_code} - {response.text}")