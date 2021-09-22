# Read the input
numbers = [x.strip() for x in open('input.txt', 'r').readlines()]

def run_part1():
    preamble = 25
    position = preamble
    is_xmas = True
    while position < len(numbers) and is_xmas:
        is_xmas = False # Assume is false, let's test
        for i in range(position-(preamble), position):
            for j in range(position-(preamble), position):
                #print(position, numbers[position], numbers[i], numbers[j],\
                      #int(numbers[i])+int(numbers[j]))
                if (int(numbers[i])+int(numbers[j])) == int(numbers[position]) and i != j:
                    is_xmas = True
        if is_xmas is False:
            #print("Not xmas:", numbers[position], position)
            target = int(numbers[position])
        position += 1
    return target


def run_part2():
    position_i = 0
    sum1 = 0
    results = []
    not_found = True
    target = run_part1()
    print('Target:', target)
    while position_i < len(numbers) and sum1 < target and not_found:
        sum1 = int(numbers[position_i])
        position_j = position_i+1
        while position_j < len(numbers) and sum1 < target:
            sum1 += int(numbers[position_j])
            #print(sum, position_i, position_j)
            if sum1 == target:
                size = position_j - position_i + 1
                for k in range(0, size):
                    results.append(int(numbers[position_i+k]))
                print('Found range:', position_i, position_j, results)
                print('Answer:', max(results) + min(results))
                not_found = False
            position_j += 1
        sum1 = 0
        position_i += 1


run_part2()
