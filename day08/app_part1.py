# Read the input
lines = [x.strip() for x in open('input.txt', 'r').readlines()]
index = 0
ran_lines = []
accumulator = 0
condition = True

while index < len(lines) and index not in ran_lines:
    command_line = lines[index].split(' ')
    #print(index, command_line[0],  command_line[1], ran_lines, condition)
    if command_line[0] == 'nop':
        ran_lines.append(index)
        index += 1
    if command_line[0] == 'acc':
        accumulator += int(command_line[1])
        ran_lines.append(index)
        index += 1
    if command_line[0] == 'jmp':
        ran_lines.append(index)
        index += int(command_line[1])

print('Accumulator value:', accumulator)
