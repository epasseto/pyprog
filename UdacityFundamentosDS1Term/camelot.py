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

#def create_cast_list(filename):
#    cast_list = []
#    with open(filename) as f:
#        for line in f:
#            name = line.split(",")[0]
#            cast_list.append(name)
#
#    return cast_list

#cast_list = create_cast_list('flying_circus_cast.txt')
#for actor in cast_list:
#    print(actor)