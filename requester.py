'''
Created on 8 de jun de 2016

@author: Frederico
'''
import requests
from bs4 import BeautifulSoup

url_post = 'http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/Controller'

data = {'acao':'calcular',
          'valor':'R$ 500,00',
          'valorINI':'01/10/1999',
          'valorFIM':'30/04/2016',
          'SELIC':'N',
          'juros':'1,00',
          'jurosINI':'01/10/1999',
          'jurosFIM':'30/04/2016',
          'honorarios':'0,00',
          'multa':'N',
          'visualizacao':'S',
          'button':'Calcular',
          'button':'Calcular'
          }
 
 
r = requests.post(url_post, data)

# print('Got ' + str(len(r.cookies)) + ' cookies!')

for c in r.cookies:
    cookie = {c.name:c.value}
#     print(cookie)
    new_url = 'http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/calculo.jsp'
    r2 = requests.get(new_url, cookies=cookie)
    soup = BeautifulSoup(r2.text.encode('UTF-8'), 'html.parser')
    resultado = soup.find('div', id='resultado').contents[1]
    print(resultado)
