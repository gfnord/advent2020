# Read the input
lines = [x.strip() for x in open('input_test.txt', 'r').readlines()]
lines = [tuple(x.split()) for x in lines]

def run(lines):
    lines_executed = set()
    index = 0
    accumulator = 0

    def acc(lines, index, accumulator):
        return (index + 1, accumulator + int(lines[index][1]))

    def jmp(lines, index, accumulator):
        return (index + int(lines[index][1]), accumulator )

    def nop(lines, index, accumulator):
        return (index + 1, accumulator)

    terminated = False
    while not terminated and index not in lines_executed:
        instruction = lines[index][0]
        lines_executed.add(index)

        operations = {
            'jmp': jmp,
            'acc': acc,
            'nop': nop,
        }
        operation = operations[instruction]
        index, accumulator = operation(lines, index, accumulator)

        # Terminate if end at program
        terminated = index == len(lines)

    return terminated, accumulator


def Part2(lines):
    for i in range(len(lines)):
        # Copy lines so that changes don't persist.
        local_lines = [x for x in lines]

        # Switch statement jmp/nop
        if 'jmp' in local_lines[i][0]:
            local_lines[i] = ('nop', local_lines[i][1])
        elif 'nop' in local_lines[i][0]:
            local_lines[i] = ('jmp', local_lines[i][1])

        terminated, result = run(local_lines)

        if terminated:
            break
    return result


print ('Answer: ', Part2(lines))
