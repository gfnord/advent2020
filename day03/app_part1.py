trees = 0

f=open("input.txt","r")
lines=f.readlines()
result = []
index_x = 1
start_x = 2
start_y = 4
increment_y = 3
increment_x = 1
slope_x = start_x
slope_y = start_y

for x in lines:
    x = x.strip() # remove end of line
    y = list(x)
    max_y = len(y)
    index_y = 1
    pattern = int(float(index_x)/float(max_y+1))
    for i in y:
        if index_x == slope_x and index_y == slope_y:
            if i == '#': # check if slope matches a tree
                print(i, index_x, index_y, end = '\n')
                trees += 1
            slope_x = slope_x + increment_x # going to next point
            slope_y = slope_y + increment_y
        if slope_y <= max_y:
            index_y += 1
        else:
            diff = slope_y - max_y
            slope_y = diff # start new pattern
    index_x += 1

print('Trees: ', trees)

f.close()
