print ("Enter names separated by commas: ")
print ("Enter assignments separated by commas: ")
print ("Enter grades separated by commas: ")

#names =  # capture e processe o input para uma lista de nomes
#assignments =  # capture e processe o input para uma lista do número de tarefas
#grades =  # capture e processe o input para uma lista de notas

# string de mensagem a ser usada para cada aluno
# DICA: use .format() com esta string no seu loop for
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# escreva um loop for que realize uma iteração em cada conjunto de nomes, tarefas e notas para imprimir a mensagem de cada aluno

print (message)



#Escreva um script que faz o seguinte:
#Pede 3 vezes uma entrada do usuário. 
#Uma para obter uma lista de nomes, outra para obter uma lista de tarefas perdidas e uma última vez para obter uma lista de notas.
#Utilize esta entrada para criar as listas names, assignments e grades.
#Use um loop para exibir a mensagem para cada aluno com os valores corretos.
#A nota potencial é simplesmente a nota atual somada ao dobro do número de atividades perdidas.