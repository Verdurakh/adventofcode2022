def read_file(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


_lines = read_file("input.txt")
#_lines = ['noop','addx 3','addx -5']
print(_lines)


cycle = 0
x_value = 1
cycles = []

WIDTH = 40
HEIGHT = 6


for line in _lines:
    command = line.split()
    start_value = x_value
    if command[0] == 'addx':
        for i in range(1):
            cycle += 1
            cycles.append((start_value, x_value))
        x_value += int(command[1])
        cycles.append((start_value, x_value))
    elif command[0] == 'noop':
        cycle += 1
        cycles.append((start_value, x_value))

_start = 20
_sum = 0
for i in range(6):
    add = cycles[_start-1]
    #print(str(_start) + ':' + str(add))
    _sum += add[0] * _start
    _start += 40
#print(_sum)

sprite_position = 0
screen = []
counter = 1
row = ''
for cycle in cycles:
    if sprite_position == counter or sprite_position+1 == counter or sprite_position+2 == counter:
        row += '#'
    else:
        row += '.'
    sprite_position = cycle[1]
    if counter % 40 == 0:
        screen.append(row)
        row = ''
        counter = 0
    counter += 1

for sc in screen:
    print(sc)


