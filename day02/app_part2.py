okay=0
failed=0

with open("input.txt") as f:
    lines=f.readlines()

result = []
for x in lines:
    x = x.strip() # remove end of line
    x = x.replace(':', '') # remove :
    x = x.replace('-', ' ') # replace - by space
    x = x.split(' ') # split

    # Part 1
    #count = x[3].count(x[2])
    ##print(x[3], x[2], 'occurences:', count)
    #if int(x[0]) <= count <= int(x[1]):
    #    okay += 1
    #else:
    #    failed += 1
    
    # Part 2
    password = list(x[3]) # split the password into a list
    if password[int(x[0])-1] == x[2] and int(x[0]) <= len(password): 
        pos1 = 'okay'
    else:
        pos1 = 'failed'

    if password[int(x[1])-1] == x[2] and int(x[1]) <= len(password):
        pos2 = 'okay'
    else:
        pos2 = 'failed'
    
    if pos1 == 'okay' or pos2 == 'okay':
        if pos1 != pos2:
            okay += 1
        else:
            failed += 1
    else:
        failed += 1

print('Okay: ', okay)
print('Failed: ', failed)
