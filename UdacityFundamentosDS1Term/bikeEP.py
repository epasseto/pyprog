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