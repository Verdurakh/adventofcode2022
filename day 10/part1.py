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

print(cycles)
_start = 20
_sum = 0
for i in range(6):
    add = cycles[_start-1]
    print(str(_start) + ':' + str(add))
    _sum += add[0] * _start
    _start += 40
print(_sum)
