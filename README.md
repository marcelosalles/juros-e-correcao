# Juros e correção monetária

Através do site: *http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/calculo.jsp?sessionId=5B545D5776C96BEE939B51C51722CF9D*


Inicialmente, eu peguei a fórmula mostrada no site e criei uma planilha de Excel.

Porém, meus valores não bateram com o do site. Pela "Visualização Analítica", os juros eram ajustados a cada mês, e eu não sei no que isso se baseava.

Então, tive a ideia de desenvolver um programa em Python para jogaria os valores no site para baixar os resultados.

A data final sempre será **30/04/2016**, os juros sempre serão **1,00 %**. As únicas variáveis serão a data inicial, e o Valor.

No resultado, só precisa pegar o **Valor Atualizado, Valor dos juros** e **Total geral**.

##EX:

Na coluna da **Correção Monetária**:
  - Valor: *500,00*
  - Data Inicial: *01/10/1999*
  - Data Final: *30/04/2016*

Na Coluna dos **Juros**:
  - Juros Mensal: *1,00*
  - De: *01/10/1999*
  - Até: *30/04/2016*

Os outros valores podem ficara em branco.

##Desenvolvimento:

A partir da análise feita via navegador Chrome, parece que o site recebe a requisição POST e redireciona o usuário algumas vezes para páginas do Google Analytics antes de exibir o resultado final. A requisição POST feita via python parece confirmar isso, pois retorna a seguinte página: 

```html
<html>
    <head>
        <meta http-equiv="refresh" content="0;url=/AtualizacaoMonetaria/calculo.jsp?sessionId=EB0CBDE0266CA0B016823B2BF8264BF0#msg">
        <script>
            (function(i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r;
                i[r] = i[r] || function() {
                    (i[r].q = i[r].q || []).push(arguments)
                }, i[r].l = 1 * new Date();
                a = s.createElement(o),
                        m = s.getElementsByTagName(o)[0];
                a.async = 1;
                a.src = g;
                m.parentNode.insertBefore(a, m)
            })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

            ga('create', 'UA-54017566-1', 'auto');
            ga('send', 'pageview');

        </script>
    </head>
    <body>
    </body>
</html>
```

Segundo esse [link](https://developers.google.com/analytics/devguides/collection/analyticsjs/advanced?hl=pt-Br#snippetReference), esse código do google analytics não parece fazer muita coisa.
É na verdade a linha `<meta http-equiv="refresh" content="0;url=/AtualizacaoMonetaria/calculo.jsp?sessionId=EB0CBDE0266CA0B016823B2BF8264BF0#msg">` que redireciona o usuário para outra página.

O problema persiste pois seguindo esse link, caímos novamente na página principal. Uma hipótese é de que a requisição não está completa e/ou correta, e portanto deve-se debugar para montar uma requisição válida. Podemos estudar a troca de dados entre cliente e servidor pelo navegador Chrome da seguinte forma:

![chrome_network](http://wpscholar.com/content/uploads/2015/07/chrome-view-post-data.gif)

Essa análise evidenciou a utilização de cookies, tanto na hora da submissão da requisição POST quanto no recebimento da página com os resultados:

![request_cookies](http://i.imgur.com/xTNlgxR.png)

Infelizmente a simples adição de uma cópia do cookie gerado pela página não gerou o resultado esperado, portanto deve-se estudar o resto do 
[cabeçalho da requisição http](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields) para tentar gerar uma requisição correta e obter os dados desejados.

Após utilizar o cookie retornado pela primeira requisição ao invés de criar um estático, o programa finalmente foi capaz de criar uma requisição válida e a página retornada continha os resultados esperados.

Para a digestão dos dados recebidos, foi utilizada a biblioteca [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), que permite fazer buscas no código html através de atributos específicos.

Agora basta modificar o programa para gerar requisições com base em uma lista pré-definida para gerar resultados de forma rápida e automática! :)

##Imagens:

Primeira requisição POST:
![post](http://i.imgur.com/OXpvdYK.png)

Após redirecionamentos, requisição GET que gera página com resultados:
![get](http://i.imgur.com/vKv2SMF.png)

##Referência:

- http://wpscholar.com/blog/view-form-data-in-chrome/
- https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields
- http://stackoverflow.com/questions/4979638/python-simple-post-method
- http://stackoverflow.com/questions/11322430/python-how-to-send-post-request
- https://developers.google.com/analytics/devguides/collection/analyticsjs/advanced?hl=pt-Br#snippetReference
