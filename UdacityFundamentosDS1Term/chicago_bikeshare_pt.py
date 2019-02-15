import csv # Começando com os imports # coding: utf-8
import matplotlib.pyplot as plt

print("Lendo o documento...") # Vamos ler os dados como uma lista
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")
print("Número de linhas:") # Vamos verificar quantas linhas nós temos
print(len(data_list))
print("Linha 0: ") # Imprimindo a primeira linha de data_list para verificar se funcionou.
print(data_list[0]) # É o cabeçalho dos dados, para que possamos identificar as colunas.
print("Linha 1: ") # Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print(data_list[1])

input("Aperte Enter para continuar...")

# TAREFA 1: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras") 
data_list = data_list[1:] # Vamos mudar o data_list para remover o cabeçalho dele. Nós podemos acessar as features pelo índice. Por exemplo: sample[6] para imprimir gênero, ou sample[-2]
for i in range(20):
	print(data_list[i])

input("Aperte Enter para continuar...")

# TAREFA 2: Imprima o `gênero` das primeiras 20 linhas (il=6)
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
a = []
for i in range(20):
	a = data_list[i]
	print (a[6]) # Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices. Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros
input("Aperte Enter para continuar...")

# TAREFA 3: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
def column_to_list(data, index):
     # Função de fatiar uma tabela de dados, por coluna (cada coluna é um campo).
     # Argumentos:
     #     data: a tabela original (nosso .CSV sem cabeçalho e transformado numa lista). É uma lista.
     #     index: a posição ocupada pelo campo do nosso interesse. É um inteiro.
     # Retorna:
     #     Uma fatia da tabela. É uma lista. 
    a = []
    column_list = [] 
    for i in range(len(data)):
        a = data[i]
        if a[index] == "":
            column_list.append("")	
        else:
            column_list.append(a[index])
    return column_list
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras") # Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...") # Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem

# TAREFA 4: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0 
female = 0
paracontar = column_to_list(data_list, -2)

#print (paracontar[:20])
#male = paracontar.count("Male")
#female = paracontar.count("Female")

#eu simplesmente crieo dois contadores e adicionei nas variáveis inteiras dadas.
for entrada in paracontar:
	if entrada == "Male":
		male += 1
	if entrada == "Female":
		female += 1

print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos") # Verificando o resultado

print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------
input("Aperte Enter para continuar...") # Por que nós não criamos uma função parTODO isso?

# TAREFA 5: Crie uma função para contar os gêneros. Retorne uma lista. Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list): 
     # Função de contagem de gêneros, a partir de uma fatia (campo) de uma tabela.
     # Argumentos:
     #     data_list: uma fatia (apenas um campo) de dados originais. É uma lista.
     # Retorna:
     #     Uma tupla (contagem de Masculino e Feminino). Dois valores inteiros. 	
    male = 0
    female = 0
    a = []
    column_list = [] 
    for i in range(len(data_list)):
        a = data_list[i]
        if a[-2] == "Male": 
            male += 1
        if a[-2] == "Female":
            female += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")

print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------
input("Aperte Enter para continuar...") # Agora que nós podemos contar os usuários, qual gênero é mais prevalente?

# TAREFA 6: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string. Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list): 
     # Esta função determina o gênero mais popular, a partir de uma fatia (campo) de uma tabela.
     # Argumentos:
     #     data_list: uma fatia (apenas um campo) de dados originais. É uma lista.
     # Retorna:
     #     O gênero mais popular. É uma string de texto.
    answer = ""    
    genero = 0
    homem, mulher = count_gender(data_list)
    #print ("homem: ",homem, "mulher: ", mulher)
    if homem > mulher:
        answer = "Masculino"
    if mulher > homem:	
        answer = "Feminino"
    if homem == mulher:
        answer = "Igual"
    return answer
 
print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Imprime gráfico por gênero
gender_list = column_to_list(data_list, -2) # Se tudo está rodando como esperado, verifique este gráfico!
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")

# TAREFA 7: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!") 
def count_user(data_list): 
     # Esta função serve para contar usuários.
     # Argumentos:
     #     data_list: uma fatia (apenas um campo) de dados originais. É uma lista.
     # Retorna:
     #     Uma tupla de números inteiros - cliente ou assinante
     # Obs: Código reaproveitado do exercício anterior, modificando as especificações.
    customer = 0
    subscriber = 0
    a = []
    column_list = [] 
    for i in range(len(data_list)):
        a = data_list[i]
        if a[-3] == "Customer": 
            customer += 1
        if a[-3] == "Subscriber":
            subscriber += 1
    return [customer, subscriber]

usuario_list = column_to_list(data_list, -3) # Se tudo está rodando como esperado, verifique este gráfico!
types = ["Customer", "Subscriber"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")

# TAREFA 8: Responda a seguinte questão
male, female = count_gender(data_list) 
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Há registros no CSV para o qual o gênero não está preenchido."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------
input("Aperte Enter para continuar...")

# TAREFA 9: Ache a duração de viagem Mínima, Máxima, Média, e Mediana. Você não deve usar funções prontas parTODO isso, como max() e min().
#def column_to_list2(data, index): #função alterada - esta converte os dados para Float - desativada: o resultado foi obtido com .map(a1,a2)
#    a = []
#    column_list = [] # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
#    for i in range(len(data)):
#        a = data[i]
#        if a[index] == "":
#            column_list.append(0.)	
#        else:
#            column_list.append(float(a[index]))
#    return column_list

trip_duration_list = column_to_list(data_list, 2) # Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
trip_duration_list = list(map(float,trip_duration_list)) #Transformados os dados para Float, pois iremos trabalhar agora com números! 

min_trip = 0. 
max_trip = 0.
mean_trip = 0.
median_trip = 0.
elem = 0.
soma = 0. #eu preciso da soma de todos os valores para a média!

#Rotina de amostra: verificar o formato e a qualidade dos dados colhidos (verificados e desativada!)
#a = []
#i = 0
#for i in range(20):
#    a = trip_duration_list[i]
#    print (a)

# Este For serve para pegar um argumento inicial para min_trip.
# Por que eu escrevi uma função para argumento inicial? Porque eu espero que ela vá iterar umas poucas vezes.
# Observe que o If dela é mais complexo do que o If do For principal. Assim eu deixo meu For principal mais leve.
# Como a quantidade de iterações do For principal é imensa, eu quero que ele fique o mais leve possível. 
for elemento in trip_duration_list: # Quero pegar um valor inicial para min_trip
	elem = float(elemento)
	if elem > 0 and min_trip == 0: # Este if é um pouco mais lento: vou usar apenas até captar um número inicial para a min_trip!
		min_trip = elem
		print ("Primeiro valor de min: ", min_trip)
		break

# Este é meu For principal. Ele é mais leve que o anterior e espero que ele tenha um bom desempenho.
# Neste eu obtenho a soma de todos os valores, a minha viajem mais longa e a mais curta.		
for elemento in trip_duration_list: # Esse é meu iterador principal!
    elem = float(elemento) # quero lidar com um flutuante!
    soma += elem
    #print (soma)	
    if elem > max_trip:
        max_trip = elem
    if elem < min_trip:
        min_trip = elem

# Como existe o risco de que o comprimento de trip_duration_list seja zero, eu faço apenas uma tentativa, antes de resolver o problema.
# Assim evito travamento do programa.		
try:
    mean_trip = soma / len(trip_duration_list)
except ZeroDivisionError:
    print("AVISO: Lista com comprimento em branco. Por favor use um número acima de zero.")
else:
    mean_trip = soma / len(trip_duration_list)

#meio = 0. # Esse aqui será o meio da minha lista para Mediana
meio = len(trip_duration_list) // 2 #quero um número inteiro, resultado de uma divisão inteira!
#print ("meio", meio)
ordem = sorted(trip_duration_list) # Vou precisar disso para a Mediana

# Usei esses códigos para testar meus resultados. Não preciso mais deles.
#for i in range (len(trip_duration_list)):
#    print (ordem[i])
#    if round(float(ordem[i])) == 670:
#        print ("Achei a posição da mediana :", i)
#        break

# Observe que eu tenho dois casos para mediana. Em um deles, minha lista é de tamanho par.
# Nesse caso, normalmente os estatísticos entregam como Mediana a média aritmética dos dois valores de medianas.
# O caso ímpar é mais fácil: a mediana é simplesmente o valor do meio de uma lista ordenada!
a = 0. #vou precisar desses caso o tamanho da minha lista seja par
b = 0.
if len(trip_duration_list) % 2 == 0: # Agora eu quero a mediana!
    print("Lista de tamanho par")
    a = ordem[meio]
    b = ordem[meio + 1]
    median_trip = a + b / 2.
else:
    print ("Lista de tamanho ímpar")
    median_trip = float(ordem[meio]) # Esse aqui é fácil, pois tenho apenas um número como mediana!

# Checklist. Usei isso no desenvolvimento. Não preciso mais dessas linhas de lembrete.
# As mantenho no texto para o caso de futuramente precisar me lembrar do que precisei fazer para desenvolver isso tudo.
# 1-Lembrar de excluir cabeçalho
# data_list = data_list[1:]	OK (feito)
# 2-Converter os dados que passaram no `column_to_list` para `float` OK (função alterada)
# 3-Fazer o parse dos números para float: 
# trip_duration_list = list(map(float,trip_duration_list))`
 
# print("Mediana :", median_trip, "Total dados e dobro:", len(trip_duration_list), meio * 2, "Mediana -, +:", ordem[meio-1], ordem[meio+1] )
	
# print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
# print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# median_trip = 670 #apenas para passar para próximo exercício. Estava dando defeito e eu precisava disso para prosseguir com os exercícios.

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...") # Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?

# TAREFA 10: Verifique quantos tipos de start_stations nós temos, usando set()

# Fiz apenas o agrupamento usando a função interna do Python de dicionarização!
# Como entrada, usei a tripa da tabela, onde haviam tipos de Usuários, já removida é claro, a linha de cabeçalho!
user_types = set(column_to_list(data_list, 3)) 

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Creio ter dado conta de uma documentação mínima do que fiz aqui. Criei funções apenas quando isso foi pedido no cabeçalho do exercício.
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
     # Função de exemplo com anotações.
     # Argumentos:
     #     param1: O primeiro parâmetro.
     #     param2: O segundo parâmetro.
     # Retorna:
     #     Uma lista de valores x.

input("Aperte Enter para continuar...")

# TAREFA 12 - Desafio! (Opcional)
# Tentei fazer isso da melhor forma que imaginei. Acredito que deu certo.
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
     # Função de contagem genérica (possibilita uma quantidade de tipos não definida inicialmente.
     # Argumentos:
     #     column_list: é a tripa de campos que eu desejo contar. String de texto, no caso.
     # Retorna:
     #     Uma tupla, composta de duas listas. A primeira, em String de texto, contendo os tipos e a segunda, os valores contados para cada tipo.
    item_types = [] # Inicializa essa lista
    tipos = set(column_list)
    for tipo in tipos: # isso aqui será minha saída dos tipos contados. Então eu leio do meu set e gravo na primeira lista de saída.
        item_types.append (tipo)	
    #for item in item_types:
        #print("tipo de item :", item)
    count_items = [] # Inicializa essa lista
    contagem = {} # Criar um dicionário dos tipos. Eu uso um dicionário para fazer minhas contagens.
    for tipo in item_types: #alimenta o dicionário com os zeros iniciais. 
        #print ("tipo :", tipo) #{"", "Male", "Female"}
        contagem[tipo] = 0
    for item in column_list:
        if item in contagem:
            contagem[item] += 1 # Adiciona um na contagem para um tipo do meu dicionário.
    for tipo in item_types: # Agora eu preciso devolver os resultados numa lista. Então ela lê do meu dicionário e adiciona na segunda lista de saída.
        count_items.append(contagem[tipo])
    return item_types, count_items

#item_types = [set(column_to_list(data_list, -2))]
#for item in item_types: #verificar se saíram os tipos
#    print (item)
	
if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
	
	####
	import math

print(math.factorial(4))

### FIM DO PROGRAMA

### Funções
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

#Bibliotecas muito usadas, de terceiros:
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

### useful_functions.py
### exemplo de uma função reaproveitável e com teste interno!
def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
	
###
#We're the knights of the round table
#We dance whenever we're able

with open("camelot.txt", "r") as song: #ou caminho inteiro: "c:/pyprog/..."
    print(song.read(2))
    print(song.read(8))
    print(song.read())
	
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

### Exemplo de função com try (para não travar)
def create_groups(items, n): #Splits items into n groups of equal size, although the last one may be shorter.
	try: # dermina o tamanho que cada grupo terá
		size = len(items) // n  # um erro de exceção ZeroDivisionError pode ocorrer
	except ZeroDivisionError as e:
		print ("um erro de divisão por zero ocorreu: {}".format(e))
		return []
	else:
		groups = [] # create each group and append to a new list
		for i in range(0, len(items), size):
			groups.append(items[i:i + size])
		return groups
	finally:
		print("{} groups returned.".format(n)) # print the number of groups and return groups    

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))

#Edite o script acima para tratar o erro de divisão por zero. Fazer isso corretamente deve resultar na saída:

#Creating 6 groups...
#6 groups returned.
#[0, 1, 2, 3, 4]
#[5, 6, 7, 8, 9]
#[10, 11, 12, 13, 14]
#[15, 16, 17, 18, 19]
#[20, 21, 22, 23, 24]
#[25, 26, 27, 28, 29]
#[30, 31]

#Creating 0 groups...
#WARNING: Returning empty list. Please use a nonzero number.
#0 groups returned."""

#try:
    # some code
#except ZeroDivisionError as e:
   # some code
 #  print("ZeroDivisionError occurred: {}".format(e))
#Isto iria exibir algo parecido com isto:

#ZeroDivisionError occurred: integer division or modulo by zero

#try:
    # some code
#except Exception as e:
   # some code
#   print("Exception occurred: {}".format(e))

###
### Uso de indexação
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# Use a indexação de lista para definir a variável num_days com quantos dias existem em um mês específico
num_days = days_in_month [month-1]
print(num_days)

### Listas
Funções úteis para listas I
len() devolve quantos elementos existem em uma lista.
max() devolve o maior elemento da lista. A maneira como é determinado o maior elemento de uma lista depende de quais tipos de objetos estão presentes na lista. O elemento máximo em uma lista de números é o maior número. O elemento máximo de uma lista de strings é o elemento que ocorreria por último caso a lista estivesse em ordem alfabética. Isso funciona porque a função máximo é definida em termos do operador de comparação ‘maior do que’. A função máximo é indefinida para listas que contêm elementos de tipos diferentes, incomparáveis.
min() devolve o menor elemento em uma lista. Mínimo é o oposto de máximo e retorna o menor elemento de uma lista.
sorted() devolve uma cópia de uma lista, ordenada do menor para o maior, deixando a lista inalterada.

###
Funções úteis para listas II
Método join
Join é um método de strings que recebe uma lista de strings como argumento e devolve uma string formada pelos elementos da lista unidos por um separador de strings.

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
Saída:

fore
aft
starboard
port
Neste exemplo, usamos a string "\n" como separador para que haja uma nova linha entre cada elemento. Podemos também utilizar outras strings como separadores com .join. Aqui, usamos um hífen.

name = "-".join(["García", "O'Kelly"])
print(name)
Saída:

García-O'Kelly
É importante lembrar de separar cada um dos itens da lista que você está unindo, usando uma vírgula (,). Esquecendo de fazer isso não vai provocar um erro, mas vai gerar resultados inesperados.

Método append
Um método útil chamado append adiciona um elemento ao final de uma lista.

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
Saída:

['a', 'b', 'c', 'd', 'z']

### Dicionários
>>> population = {'Shanghai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}
Optei por colocar cada par chave-valor em sua própria linha para facilitar a leitura desta definição de dicionário, mas, onde e se você usa quebras de linha é simplesmente uma escolha estilística. Este código funciona tão bem quanto:

>>> population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

### 
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
elements["hydrogen"]["is_noble_gas"]= "False"
elements["helium"]["is_noble_gas"]= "True"

print(elements["hydrogen"]["is_noble_gas"])
print(elements["helium"]["is_noble_gas"])
# todo: Adicione uma entrada 'is_noble_gas' para hydrogen e helium identificando se são gases nobres
# dica: helium é um gás nobre, hydrogênio não

### Função .zip()
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
element = ("",0,0,0)

for point in zip(labels, x_coord, y_coord, z_coord):
    element = (("{0}: {1}, {2}, {3}".format(*point))) #<-é uma string formatada!
    #element = (point[0]+": "+str(point[1])+", "+str(point[2])+", "+str(point[3]))
    #print (element)
    points.append(element)

#for point in zip(labels, x_coord, y_coord, z_coord):
#    points.append(("{}: {}, {}, {}".format(*point)))
for point in points:
    print(point)
	
### Exemplo de saída formatada
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)
	
### Compreensão de listas
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name[:name.find(" ")].lower() for name in names]
print(first_names)

### Função Lambda
#Com uma expressão lambda, esta função:
def multiply(x, y):
    return x * y
#pode ser reduzida para:
multiply = lambda x, y: x * y
#Componentes de uma função lambda
#A palavra-chave lambda é utilizada para indicar que se trata de uma expressão lambda.
#Depois de lambda, temos um ou mais argumentos para a função anônima, separados por vírgulas e seguidos por dois pontos :. Semelhante às funções, a maneira como os argumentos são nomeados em uma expressão lambda é arbitrária.
#Por último está uma expressão que é avaliada e devolvida nessa função. Isto se parece muito com uma expressão que você pode ver como declaração de retorno em uma função.
#Com essa estrutura, as expressões lambda não são ideais para funções complexas, mas podem ser muito úteis para funções curtas e simples.

### Exemplo de uso de função Lambda
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

#def mean(num_list):
#    return sum(num_list) / len(num_list)
#averages = list(map(mean, numbers))

averages = list(map(lambda num_list: sum(num_list)/len(num_list), numbers))
print(averages)


### Solução do quiz: Lambda com mapa
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)
#Saída: [57.0, 58.2, 50.6, 27.2]

###Solução do quiz: Lambda com filtro
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
#Saída: ['Chicago', 'Denver', 'Boston']

### Iterador
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def enumerador(iteravel, inicio=0):
    contador = inicio
    for elemento in iteravel:
        yield contador, elemento
        contador += 1

for i, lesson in enumerador(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
    
#sq_iterator = (x**2 for x in range(10))  # isto produz um iterador de quadrados
#print (sq_iterator)

### Solução do quiz: Implementando my_enumerate
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
#Saída:
#Lesson 1: Why Python Programming
#Lesson 2: Data Types and Operators
#Lesson 3: Control Flow
#Lesson 4: Functions
#Lesson 5: Scripting
#Solução do quiz: Chunker
#Aqui está uma maneira de você fazer isso. Você pode encontrar essa implementação nesta página do Stack Overflow.

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
#Saída:
#[0, 1, 2, 3]
#[4, 5, 6, 7]
#[8, 9, 10, 11]
#[12, 13, 14, 15]
#[16, 17, 18, 19]
#[20, 21, 22, 23]
#[24]

### Gerador de expressões
#Aqui está um conceito legal que combina geradores e compreensão de listas! Na verdade, você pode criar um gerador da mesma maneira que normalmente escreveria uma compreensão da lista, utilizando parênteses em vez de colchetes. Por exemplo:
sq_list = [x**2 for x in range(10)]  # isto produz uma lista de quadrados
sq_iterator = (x**2 for x in range(10))  # isto produz um iterador de quadrados
#Isso pode ajudá-lo a economizar tempo e criar um código eficiente!

### Scripting com entrada
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

### Lidar com erros
#Declaração try
#Podemos utilizar declarações try para lidar com exceções. Existem quatro cláusulas que você pode usar (uma além daquelas mostrados no vídeo).

#try: Essa é a única clausula mandatória em uma declaração try. O código neste bloco é a primeira coisa que o Python executa em uma declaração try.
#except: Se o Python encontra uma exceção durante a execução do bloco try, ele vai saltar para o bloco except que lida com aquela exceção.
#else: Se o Python não encontra exceções durante a execução do bloco try, ele executará o código neste bloco depois de executar o bloco try.
#finally: Antes de o Python sair da declaração try, ele executará o código deste bloco finally sob quaisquer condições, mesmo se estiver finalizando o programa. Por exemplo, se o Python encontrou um erro durante a execução do código do bloco except ou else , este bloco finally ainda será executado antes da interrupção do programa.

###	Solução do quiz: Lidando com a divisão por zero
def create_groups(items, n):
    try:
        size = len(items) // n
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
        return []
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(n))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
#Saída:
#Creating 6 groups...
#6 groups returned.
#[0, 1, 2, 3, 4]
#[5, 6, 7, 8, 9]
#[10, 11, 12, 13, 14]
#[15, 16, 17, 18, 19]
#[20, 21, 22, 23, 24]
#[25, 26, 27, 28, 29]
#[30, 31]

#Creating 0 groups...
#WARNING: Returning empty list. Please use a nonzero number.
#0 groups returned.
	
#Acessando as mensagens de erro
#Quando você lida com uma exceção, ainda pode acessar sua mensagem de erro desta forma:

try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
#Isto iria exibir algo parecido com isto:

#ZeroDivisionError occurred: integer division or modulo by zero
#Então, você ainda pode acessar as mensagens de erro, mesmo que lide com eles para evitar que seu programa seja interrompido!

#Se você não tiver um erro específico com o qual está lidando, ainda pode acessar a mensagem assim:

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
#Exception é a classe base para todas as exceções internas. Você pode aprender mais sobre as exceções do Python aqui.

###
Recorrendo ao métodoread com um número inteiro
No código que você viu anteriormente, a recorrência à f.read() não apresentava argumentos passados para ela. Isso resulta no padrão de leitura de todo o restante do arquivo a partir de sua posição atual - o arquivo inteiro. Se você entra com um argumento do tipo inteiro no método read, ele é lido até atingir aquele número de caracteres, retorna todos eles e mantém a 'janela' naquela posição, pronta para continuar lendo.

Vamos ver isso em um exemplo que utiliza o seguinte arquivo, camelot.txt:

We're the knights of the round table
We dance whenever we're able
Aqui está um script que lê o arquivo um pouco de cada vez, passando um argumento inteiro para .read().

with open(camelot.txt) as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
Saídas:

We
're the 
knights of the round table
We dance whenever we're able
Você pode treinar isso criando seus próprios arquivos camelot.txt e example.py com o texto acima.

A cada vez que utilizamos read no arquivo com um argumento inteiro, ele leu até aquele determinado número de caracteres, retornou-os e manteve a 'janela' naquela posição para a próxima utilização de read. Isso faz com que a movimentação pelo arquivo aberto seja um tanto complicada, pois não existem muitas referências na hora de navegar.

Lendo linha por linha
\n em blocos de texto são caracteres indicando uma nova linha. O caractere de nova linha marca o final de uma linha e diz para um programa (como um editor de texto) passar para a próxima linha. No entanto, olhando para o fluxo de caracteres no arquivo, \n é só mais um carácter.

### Lendo e escrevendo arquivos
Solução do quiz: Lista do elenco de Flying Circus
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
	
### Importando biblioteca padrão
Importando scripts locais
Na realidade, podemos importar códigos Python de outros scripts, o que é útil se você estiver trabalhando em um projeto maior no qual você deseja organizar seu código em vários arquivos e reutilizar esses códigos. Se o script Python que você deseja importar estiver no mesmo diretório que o script atual, apenas digite import seguido do nome do arquivo sem a extensão .py.

import useful_functions
É a convenção padrão que declarações import sejam escritas na parte superior de um script Python, um em cada linha separada. Esta declaração import cria um objeto de módulo chamado useful_functions. Módulos são apenas arquivos de Python que contêm definições e declarações. Para acessar objetos de módulos importados, você precisa utilizar a notação de ponto.

import useful_functions
useful_functions.add_five([1, 2, 3, 4])
Podemos adicionar um apelido a um módulo importado para recorrer a ele com um nome diferente.

import useful_functions as uf
uf.add_five([1, 2, 3, 4])
Utilizando um bloco principal
Para evitar a execução de declarações executáveis de um script quando elas foram importadas como um módulo em outro script, inclua essas linhas em um bloco if __name__ == "__main__". Ou, alternativamente, inclua-os em uma função chamada main() e utilize-a no bloco if main.

Sempre que podemos executar um script como este, o Python na verdade define uma variável interna especial chamada __name__ para qualquer módulo. Quando executamos um script, o Python reconhece este módulo como o programa principal e define a variável __name__ para este módulo para a string “__main__”. Para quaisquer módulos importados neste script, essa variável interna __name__ só é definida para o nome desse módulo. Portanto, a condição de if __name__ == "__main__" só está checando se este módulo é o programa principal.

Tente você mesmo!
Aqui está o código que eu usei no vídeo acima. Crie esses scripts no mesmo diretório e os execute em seu terminal! Experimente com o bloco if main e acesse objetos do módulo importado!

# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)
# useful_functions.py

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
	
### Biblioteca padrão
#Solução do quiz: Gerador de senha
#Para criar senhas aleatórias, usamos import random. A definição da função era simplesmente:

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
Como alternativa, você pode usar a função random.sample e o método .join para strings:

def generate_password():
    return ''.join(random.sample(word_list,3))
	
	
### Importar Módulos
#Técnicas para a importação de módulos
#Existem outras variantes de declarações import que são úteis em diferentes situações.

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
from module_name

### Bibliotecas de terceiros
#Existem dezenas de milhares de bibliotecas de terceiros escritas por desenvolvedores independentes! Você pode instalá-las usando o pip, um gerenciador de pacotes que está incluso no Python 3. O pip é o gerenciador de pacotes padrão para o Python, mas não é o único. Uma alternativa popular é o Anaconda, que é projetado especificamente para ciência de dados.

#Para instalar um pacote usando o pip, basta digitar "pip install" seguido do nome do pacote em sua linha de comando, assim: pip install package_name. Isso baixa e instala o pacote para que ele esteja disponível para importação em seus programas. Uma vez instalado, você pode importar pacotes de terceiros usando a mesma sintaxe usada para importar da biblioteca padrão.

#Usando um arquivo requirements.txt
#Programas maiores em Python podem depender de dezenas de pacotes de terceiros. Para facilitar o compartilhamento desses programas, os programadores frequentemente listam as dependências do projeto em um arquivo chamado requirements.txt. Este é um exemplo de um arquivo requirements.txt.

#beautifulsoup4==4.5.1
#bs4==0.0.1
#pytz==2016.7
#requests==2.11.1
#Cada linha do arquivo inclui o nome de um pacote e seu número de versão. O número de versão é opcional, mas geralmente é incluído. Bibliotecas podem mudar sutilmente ou drasticamente entre as versões, por isso, é importante usar as mesmas versões de biblioteca que foram utilizadas para escrever o programa.

#Você pode usar o pip para instalar todas as dependências do projeto ao mesmo tempo, digitando pip install -r requirements.txt em sua linha de comando.

### Pacotes úteis de terceiros
#Ser capaz de instalar e importar bibliotecas de terceiros é útil, mas, para ser um programador eficaz, você também precisa saber quais bibliotecas estão disponíveis uso. As pessoas geralmente aprendem sobre novas bibliotecas úteis por meio de recomendações online ou de colegas. Se você for um programador novo em Python, pode não ter muitos colegas, então, para começar, aqui está uma lista de pacotes que são populares entre os engenheiros da Udacity.

#IPython - um interpretador interativo do Python.
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