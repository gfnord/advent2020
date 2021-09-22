def calc_slope(name, _start_x, _start_y, _increment_x, _increment_y):
    with open("input.txt") as f:
        lines=f.readlines()
    slope_name = name
    trees = 0
    index_x = 1
    start_x = _start_x
    start_y = _start_y
    increment_x = _increment_x
    increment_y = _increment_y
    slope_x = start_x
    slope_y = start_y

    #print('Slope name: ', slope_name)
    #print('start x:', start_x, 'start y:', start_y)
    #print('increment x:', increment_x, 'increment y:', increment_y)
    for x in lines:
        x = x.strip() # remove end of line
        y = list(x)
        max_y = len(y)
        index_y = 1
        for i in y:
            if index_x == slope_x and index_y == slope_y:
                if i == '#': # check if slope matches a tree
                    #print(i, index_x, index_y, end = '\n')
                    trees += 1
                slope_x = slope_x + increment_x # going to next point
                slope_y = slope_y + increment_y
            if slope_y <= max_y:
                index_y += 1
            else:
                diff = slope_y - max_y
                slope_y = diff # start new pattern
        index_x += 1
    print('Slope:', slope_name, 'Trees:', trees)
    return trees

trees1 = calc_slope("Track1", 2, 2, 1, 1)
trees2 = calc_slope("Track2", 2, 4, 1, 3)
trees3 = calc_slope("Track3", 2, 6, 1, 5)
trees4 = calc_slope("Track4", 2, 8, 1, 7)
trees5 = calc_slope("Track5", 3, 2, 2, 1)

print ('Answer:', trees1*trees2*trees3*trees4*trees5)
