lista = [] # define empty list

with open("list.txt") as f: # open input file
    lista = f.readlines() # read content and add to list
    lista = [x.strip() for x in lista] # remove end of line
    lista = [int(x) for x in lista] # convert to integer

for x in range(len(lista)): 
    for y in range(len(lista)):
        if lista[x] + lista[y] == 2020:
            print(lista[x], " and ", lista[y], " : multiplication is ", lista[x] * lista[y])        

for x in range(len(lista)):
    for y in range(len(lista)):
        for z in range(len(lista)):
            if lista[x] + lista[y] + lista[z] == 2020:
                print(lista[x], ",", lista [y]," and ", lista[z], " : multiplication is ", lista[x] * lista[y] * lista[z])
