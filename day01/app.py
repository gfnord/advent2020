lista = [] # define empty list

with open("list.txt") as f: # open input file
    lista = f.readlines() # read content and add to list
    lista = [x.strip() for x in lista] # remove end of line
    lista = [int(x) for x in lista] # convert to integer

for x, valuex in enumerate(lista):
    for y, valuey in enumerate(lista):
        if valuex + valuey == 2020:
            print(valuex, " and ", valuey, " : multiplication is ",
                  valuex * valuey)

for x, valuex in enumerate(lista):
    for y, valuey in enumerate(lista):
        for z, valuez in enumerate(lista):
            if valuex + valuey + valuez == 2020:
                print(valuex, ",", valuey," and ",valuez,
                      " : multiplication is ", valuex * valuey * valuez)
