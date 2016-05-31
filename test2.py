import requests

url = 'http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/calculo.jsp?sessionId=A3AE5A4568FF94EF79D2BF285FCD8642'
url_post = 'http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/Controller?sessionId=A3AE5A4568FF94EF79D2BF285FCD8642'

header = {'Referer': 'http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/Controller?sessionId=A3AE5A4568FF94EF79D2BF285FCD8642',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
          'Host':'cgjweb.tjsc.jus.br'
          }
cookie = {'JSESSIONID': 'A3AE5A4568FF94EF79D2BF285FCD8642',
          '_ga': 'GA1.3.1064966475.1463173013',
          '_gat': '1',
#           'dtCookie': 'F0F12C4F081634E0767965905DC5F39D|X2RlZmF1bHR8MQ'
          'dtCookie': 'F0F12C4F081634E0767965905DC5F39D'
          }
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
 
 
# r = requests.get(url, headers=header, cookies=cookie)
r = requests.post(url_post, data, headers=header, cookies=cookie)

print(r.text.encode('UTF-8')) 