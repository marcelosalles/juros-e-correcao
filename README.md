# Juros e correção monetária

Através do site: *http://cgjweb.tjsc.jus.br/AtualizacaoMonetaria/calculo.jsp?sessionId=5B545D5776C96BEE939B51C51722CF9D*


Inicialmente, eu peguei a fórmula mostrada no site e criei uma planilha de Excel.

Porém, meus valores não bateram com o do site. Pela "Visualização Analítica", os juros eram ajustados a cada mês, e eu não sei no que isso se baseava.

Então, tive a ideia de desenvolver um programa em Python para jogaria os valores no site para baixar os resultados.

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
