"""
>>> from bs4 import BeatifulSoup

>>> html_file = open("generic_simple.html", mode="r", encoding="utf-8")
>>> html_file
<_io.TextIOWrapper name='generic_simple.html' mode='r' encoding='utf-8'>

>>> soup = BeautifulSoup(html_file) 
>>> soup
<!DOCTYPE html>

<html>
<head>
<title>Um HTML simples</title>
</head>
<body bgcolor="salmon">
<h1 style="background-color:peachpuff">Um tópico aleatório</h1>
<div class="article" id="I_AM_Unique" style="background-color:peachpuff">
<p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.  
                Ainda assim, se você está lendo, o problema é seu.
                Você ainda não consegue descobrir, eu sou inútil?
                Pessoal, parem de me ler agora.
                Obrigado
        </p>
</div>
<br/><br/><br/>
<div class="article" id="imp_article_ID" style="background-color:peachpuff">
<h2>Já utilizou o google hoje?</h2>
<a href="http://www.google.com"><h3><b> Ir para o google </b></h3></a>
</div>
<br/><br/><br/>
<div class="article" id="I_AM_AnotherDivID" style="background-color:peachpuff">
<b>Sou apenas uma nova divisão<b><br/>
        Quer ir para o site do professor?
        <a href="https://www.udemy.com/user/gabriel-henrique-casemiro/">Ir agora</a>

</b></b></div>
<div class="article" id="I_AM_AnotherDivID" style="background-color:peachpuff">
<b>Vamos participar do grupo do curso?<b><br/>
<a href="https://t.me/criandoroboscompython">Entrar no grupo do telegram</a>

</b></b></div>
<br/><br/><br/>
<div id="footer" style="background-color:peachpuff">
<center><h2>Sou um rodapé</h2> </center>
</div>
</body>
</html>

>>> soup.prettify
<bound method Tag.prettify of <!DOCTYPE html>

<html>
<head>
<title>Um HTML simples</title>
</head>
<body bgcolor="salmon">
<h1 style="background-color:peachpuff">Um tópico aleatório</h1>
<div class="article" id="I_AM_Unique" style="background-color:peachpuff">
<p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.
                Ainda assim, se você está lendo, o problema é seu.
                Você ainda não consegue descobrir, eu sou inútil?
                Pessoal, parem de me ler agora.
                Obrigado
        </p>
</div>
<br/><br/><br/>
<div class="article" id="imp_article_ID" style="background-color:peachpuff">
<h2>Já utilizou o google hoje?</h2>
<a href="http://www.google.com"><h3><b> Ir para o google </b></h3></a>
</div>
<br/><br/><br/>
<div class="article" id="I_AM_AnotherDivID" style="background-color:peachpuff">
<b>Sou apenas uma nova divisão<b><br/>
        Quer ir para o site do professor?
        <a href="https://www.udemy.com/user/gabriel-henrique-casemiro/">Ir agora</a>

</b></b></div>
<div class="article" id="I_AM_AnotherDivID" style="background-color:peachpuff">
<b>Vamos participar do grupo do curso?<b><br/>
<a href="https://t.me/criandoroboscompython">Entrar no grupo do telegram</a>

</b></b></div>
<br/><br/><br/>
<div id="footer" style="background-color:peachpuff">
<center><h2>Sou um rodapé</h2> </center>
</div>
</body>
</html>

>>> soup.prettify()  #quebras de linha

>>> soup.get_text()
'\n\n\nUm HTML simples\n\n\nUm tópico aleatório\n\nEu sou a 
descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.
\n\t\tAinda assim, se você está lendo, o problema é seu.\n\t\tVocê ainda não 
consegue descobrir, eu sou inútil?\n\t\tPessoal, parem de me ler agora.
\n\t\tObrigado\n\t\n\n\n\nJá utilizou o google hoje?\n Ir para o google
\n\n\n\nSou apenas uma nova divisão\n\tQuer ir para o site do professor?\n\tIr agora\n\n\n\nVamos
participar do grupo do curso?\nEntrar no grupo do telegram\n\n\n\n\nSou um rodapé \n\n\n\n'

ou 

>>> soup.get_text().replace ("/n, "")
'\n\n\nUm HTML simples\n\n\nUm tópico aleatório\n\nEu sou a
descrição do tópico aleatório acima. Não há necessidade de me
ler em tudo.\n\t\tAinda assim, se você está lendo, o problema é seu.
\n\t\tVocê ainda não consegue descobrir, eu sou inútil?\n\t\tPessoal,
parem de me ler agora.\n\t\tObrigado\n\t\n\n\n\nJá utilizou o google hoje?\n 
Ir para o google \n\n\n\nSou apenas uma nova divisão\n\tQuer ir para o site do professor?
\n\tIr agora\n\n\n\nVamos participar do grupo do curso?\nEntrar no grupo do telegram\n\n\n\n\n
Sou um rodapé \n\n\n\n'


>>> soup.title
<title>Um HTML simples</title>

>>> soup.div
<div class="article" id="I_AM_Unique" style="background-color:peachpuff">
<p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em tudo.  
                Ainda assim, se você está lendo, o problema é seu.
                Você ainda não consegue descobrir, eu sou inútil?
                Pessoal, parem de me ler agora.
                Obrigado
        </p>
</div>


>>> list(soup.div.children)
['\n', <p style="background-color:peachpuff">Eu sou a descrição do tópico aleatório acima. Não há necessidade de me ler em 
tudo.
                Ainda assim, se você está lendo, o problema é seu.
                Você ainda não consegue descobrir, eu sou inútil?
                Pessoal, parem de me ler agora.
                Obrigado
        </p>, '\n']
        
>>> for i in list(soup.div.children): 
...     print(i.name)
... 
None
p
None

>>>soup.a
<a href="http://www.google.com"><h3><b> Ir para o google </b></h3></a>

"""
