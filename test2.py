import requests

url = "http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/Controller?sessionId=A3AE5A4568FF94EF79D2BF285FCD8642"
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
r = requests.post(url, data)

print(r.text) 