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


