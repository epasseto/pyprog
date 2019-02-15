import math

print(math.factorial(4))

#favoritas
#csv: muito conveniente para ler e gravar arquivos csv
#collections: extensões úteis dos tipos comuns de dados, incluindo OrderedDict, defaultdict e namedtuple
#random: gera números pseudoaleatórios, mistura sequências aleatoriamente e seleciona itens de maneira aleatória
#string: mais funções para strings. Este módulo também contém coleções úteis de letras como string.digits (uma string que contém todos os caracteres que são dígitos válidos).
#re: correspondência de padrões em strings através de expressões regulares
#math: algumas funções matemáticas padrão
#os: interagindo com sistemas operacionais
#os.path: submódulo de os para alterar o nome de caminhos
#sys: trabalha diretamente com o interpretador do Python
#json: bom para ler e escrever arquivos json (bom para trabalhos na web)

#Para importar uma função individual ou a uma classe de um módulo:
from module_name import object_name

#Para importar múltiplos objetos individuais de um módulo:
from module_name import first_object, second_object

#Para renomear um módulo:
import module_name as new_name

#Para importar um objeto de um módulo e renomeá-lo:
from module_name import object_name as new_name

#Para importar cada objeto individualmente de um módulo (NÃO FAÇA ISSO):
from module_name import *
#Se você realmente quiser usar todos os objetos de um módulo, use a declaração de importação padrão module_name e acesse cada um dos objetos com a notação de ponto.

#Módulos, pacotes e nomes
#Para gerenciar melhor o código, os módulos da biblioteca padrão do Python estão divididos em submódulos que estão contidos dentro de um pacote.
#Um pacote é simplesmente um módulo que contém submódulos. Um submódulo é especificado com a notação habitual de ponto.

#Módulos que são submódulos são especificados pelo nome do pacote seguido pelo nome do submódulo separados por um ponto.
#Você pode importar o submódulo assim.

import package_name.submodule_name

#pacotes de terceiros:
pip install pytz

#requirements.txt
beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1

#para instalar requirements:
pip install -r requirements.txt

#muito usadas, de terceiros:
#Python - um interpretador interativo do Python.
#requests - fornece métodos fáceis de usar para fazer solicitações na web. Útil para acessar APIs da web.
#Flask - uma estrutura leve para fazer aplicações web e APIs.
#Django - uma estrutura mais recheada de recursos para criar aplicações web. O Django é particularmente bom para projetar aplicações web complexas e com muito conteúdo.
#Beautiful Soup - usado para analisar HTML e extrair informações a partir daí. Ótimo para web scraping.
#pytest - estende os módulos de assertivas internas e testes de unidade (unittest) do Python.
#PyYAML - para ler e gravar arquivos YAML.
#NumPy - o pacote fundamental para a computação científica com Python. Ele contém, entre outras coisas, um poderoso objeto array N-dimensional e capacidades úteis para álgebra linear.
#pandas - uma biblioteca contendo ferramentas de alto desempenho, para estruturas de dados e de análise de dados. O Pandas, em especial, fornece dataframes!
#matplotlib - uma biblioteca de plotagem 2D que produz figuras com qualidade de publicação em uma variedade de formatos em papel e ambientes interativos.
#ggplot - outra biblioteca de plotagem 2D, com base na biblioteca ggplot2 do software R.
#Pillow - a biblioteca de imagens do Python adiciona capacidades de processamento de imagens a seu interpretador Python.
#pyglet - uma estrutura de aplicação multiplataforma voltada ao desenvolvimento de jogos
#Pygame - um conjunto de módulos Python projetados para escrever jogos.
#pytz - definições de fuso horário do mundo para Python

#ipython (no Anaconda):
#conclusão de guia
#? para obter detalhes sobre um objeto
#! para executar comandos shell do sistema
#realce de sintaxe!

#fontes seguras de consulta:
#The Python Tutorial - Esta seção da documentação oficial pesquisa a sintaxe do Python e a biblioteca padrão. Ela usa exemplos e é escrita usando uma linguagem menos técnica do que a documentação principal. Certifique-se de que você está lendo a versão das documentações para o Python 3!
#2:
#The Python Language and Library References - as referências de linguagem e de biblioteca são mais técnicas do que o tutorial, mas são as fontes definitivas de verdade. Conforme você se torna cada vez mais familiarizado com o Python, deve usar esses recursos cada vez mais.
#...
#Documentação de bibliotecas de terceiros- bibliotecas de terceiros publicam sua documentação em seus próprios sites e, muitas vezes, em https://readthedocs.org/. Você pode julgar a qualidade de uma biblioteca de terceiros pela qualidade de sua documentação. Se os desenvolvedores ainda não encontraram tempo para escrever boas documentações, eles provavelmente ainda não encontraram tempo para refinar sua biblioteca também.
#Sites e blogs de especialistas proeminentes - os recursos anteriores são fontes primárias, significando que são documentações das mesmas pessoas que escreveram o código que está sendo documentado. Fontes primárias são as mais confiáveis. As fontes secundárias também são extremamente valiosas. A dificuldade com as fontes secundárias é determinar sua credibilidade. Sites de autores como Doug Hellmann e desenvolvedores como Eli Bendersky são excelentes. O blog de um autor desconhecido pode ser excelente ou um lixo.
#StackOverflow- este site de perguntas e respostas tem uma boa quantidade de tráfego, então, é provável que alguém tenha feito (e alguém tenha respondido a) uma pergunta semelhante anteriormente! No entanto, as respostas são fornecidas por voluntários e variam em qualidade. Sempre entenda as soluções antes de implementá-las em seu programa. Respostas de apenas uma linha, sem qualquer explicação, são duvidosas. Este é um bom lugar para descobrir mais sobre sua dúvida ou encontrar termos de pesquisa alternativos.
#Monitoramento de bugs - às vezes, você encontrará um problema tão raro, ou tão novo, que ninguém abordou ainda no StackOverflow. Por exemplo, você pode encontrar uma referência a seu erro em um relatório de bug no GitHub. Estes relatórios de bug podem ser úteis, mas você provavelmente vai ter que fazer algum trabalho original de engenharia para solucionar o problema.
#Fóruns aleatórios - algumas vezes, sua pesquisa produz referências a fóruns que não estão ativos desde 2004, ou algum outro tempo tão antigo quanto. Caso estes sejam os únicos recursos que abordam seu problema, talvez você deva repensar como tem abordado a solução.