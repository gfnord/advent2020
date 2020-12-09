# Read the input
numbers = [x.strip() for x in open('input.txt', 'r').readlines()]
preamble = 25
position = preamble

is_xmas = True

while position < len(numbers) and is_xmas:
    is_xmas = False # Assume is false, let's test
    for i in range(position-(preamble), position):
        for j in range(position-(preamble), position):
            #print(position, numbers[position], numbers[i], numbers[j], int(numbers[i])+int(numbers[j]))
            if (int(numbers[i])+int(numbers[j])) == int(numbers[position]) and i != j:
                is_xmas = True
    if is_xmas == False:
        print("Not xmas:", numbers[position], position)
    position += 1
