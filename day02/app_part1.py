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
    count = x[3].count(x[2])
    #print(x[3], x[2], 'occurences:', count)
    if int(x[0]) <= count <= int(x[1]):
        okay += 1
    else:
        failed += 1

print('Okay: ', okay)
print('Failed: ', failed)
