import json, requests
import xml.etree.ElementTree as et
from datetime import datetime, timedelta

CEP = input('Digite o cep desejado: ')

REQUISICAO = requests.get('https://viacep.com.br/ws/'+CEP+'/json/')

RESPOSTA = json.loads(REQUISICAO.text)

#print(RESPOSTA)

#LOGRADOURO = RESPOSTA['logradouro']
LOCALIDADE = RESPOSTA['localidade']
ESTADO = RESPOSTA['uf']
print('A cidade é: '+LOCALIDADE+', o estado é: '+ESTADO)



REQUISICAO_COD = requests.get('http://servicos.cptec.inpe.br/XML/listaCidades?city='+LOCALIDADE.lower())
txtxml = REQUISICAO_COD.content
#print(txtxml)
XML = txtxml.decode('ISO-8859-1')

VALOR = et.fromstring(XML)
CIDADE = VALOR.find('.//cidade[nome="'+LOCALIDADE+'"]')
ID = CIDADE.find('id').text
#print(ID)

REQ_MET = requests.get('http://servicos.cptec.inpe.br/XML/cidade/'+ID+'/previsao.xml')
XML_REQ = REQ_MET.content
#print(XML_REQ)
XML_REQ_DEC = XML_REQ.decode('ISO 8859-1')
#print(XML_REQ_DEC)

HOJE = datetime.now().date()
print('A data de hoje é: '+str(HOJE))
AMANHA = str(HOJE + timedelta(days=1))
#print(AMANHA)

ROOT = et.fromstring(XML_REQ_DEC)
AMANHA_MAX = ROOT.find('.//previsao[dia="'+AMANHA+'"]')
AMANHA_MAX_VALOR = AMANHA_MAX.find('maxima').text
AMANHA_MIN_VALOR = AMANHA_MAX.find('minima').text
TEMPO = AMANHA_MAX.find('tempo').text
print('Amanha a temperatura máxima será de '+AMANHA_MAX_VALOR+'°C e temperatura mínima de '+AMANHA_MIN_VALOR+'°C.')
#print(TEMPO)
if TEMPO == 'ec':
    print('O tempo esta encoberto com chuvas isoladas.')
elif TEMPO == 'ci':
    print('O tempo esta com chuvas isoladas.')
elif TEMPO == 'c':
    print('O tempo esta chuvoso.')
elif TEMPO == 'in':
    print('O tempo esta instável.')
elif TEMPO == 'pp':
    print('O tempo esta com possibilidade de pancadas de chuva.')
elif TEMPO == 'cm':
    print('O tempo esta com chuvas pela manhã.')
elif TEMPO == 'cn':
    print('O tempo esta com chuvas pela noite.')
elif TEMPO == 'pt':
    print('O tempo esta com pacadas de chuva a tarde.')
elif TEMPO == 'pm':
    print('O tempo esta com pancadas de chuva pela manhã.')
elif TEMPO == 'np':
    print('O tempo esta nublado com pancadas de chuva.')
elif TEMPO == 'pc':
    print('O tempo esta com pancadas de chuva.')
elif TEMPO == 'pn':
    print('O tempo esta parcialmente nublado.')
elif TEMPO == 'cv':
    print('O tempo esta com chuviscos.')
elif TEMPO == 'ch':
    print('O tempo esta chuvoso.')
elif TEMPO == 't':
    print('O tempo esta com tempestade.')
elif TEMPO == 'ps':
    print('O tempo esta com predomínio de sol.')
elif TEMPO == 'e':
    print('O tempo esta encoberto.')
elif TEMPO == 'n':
    print('O tempo esta nublado.')
elif TEMPO == 'cl':
    print('O tempo esta com céu claro.')
elif TEMPO == 'nv':
    print('O tempo esta com nevoeiro.')
elif TEMPO == 'g':
    print('O tempo esta com geada.')
elif TEMPO == 'ne':
    print('O tempo esta com neve.')
elif TEMPO == 'nd':
    print('O tempo esta não definido.')
elif TEMPO == 'pnt':
    print('O tempo esta com pancadas de chuva a noite.')
elif TEMPO == 'psc':
    print('O tempo esta com possibilidade de chuva.')
elif TEMPO == 'pcm':
    print('O tempo esta com possibilidade de chuva pela manha.')
elif TEMPO == 'pct':
    print('O tempo esta com possibilidade de chuva a tarde.')
elif TEMPO == 'pcn':
    print('O tempo esta com possibilidade de chuva a noite.')
elif TEMPO == 'npt':
    print('O tempo esta nublado com pancadas a tarde.')
elif TEMPO == 'npn':
    print('O tempo esta nublado com pancadas a noite.')
elif TEMPO == 'ncn':
    print('O tempo esta nublado com possibilidade de chuva a noite.')
elif TEMPO == 'nct':
    print('O tempo esta nublado com possibilidade de chuva a tarde.')
elif TEMPO == 'ncm':
    print('O tempo esta com possibilidade de chuva pela manhã.')
elif TEMPO == 'npm':
    print('O tempo esta nublado com pancadas pela manhã.')
elif TEMPO == 'npp':
    print('O tempo esta nublado com possibilidade de chuva.')
elif TEMPO == 'vn':
    print('O tempo esta com variação de nebulosidade.')
elif TEMPO == 'ct':
    print('O tempo esta com chuva a tarde.')
elif TEMPO == 'ppn':
    print('O tempo esta com possibilidade de chuva a noite.')
elif TEMPO == 'ppt':
    print('O tempo esta com possibilidade de chuva a tarde.')
elif TEMPO == 'ppm':
    print('O tempo esta com possibilidade de chuva pela manhã.')