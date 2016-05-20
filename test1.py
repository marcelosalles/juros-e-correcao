import urllib
import urllib2

# http://wpscholar.com/blog/view-form-data-in-chrome/

# url = 'http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/calculo.jsp?sessionId=5B545D5776C96BEE939B51C51722CF9D'
url = 'http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/Controller?sessionId=A3AE5A4568FF94EF79D2BF285FCD8642'

values = {'acao':'calcular',
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

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

# html_file = open('page.html', 'w')
# html_file.write(the_page)
# html_file.close()

print(the_page)