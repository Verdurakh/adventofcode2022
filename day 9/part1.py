import math


def read_file(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


class Knot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.positions = set()


def move_tail3(head: Knot, tail: Knot):
    if head.x == tail.x:
        if head.y > tail.y:
            tail.y += 1
        else:
            tail.y -= 1
    elif head.y == tail.y:
        if head.x > tail.x:
            tail.x += 1
        else:
            tail.x -= 1
    else:
        if head.x > tail.x:
            tail.x += 1
        else:
            tail.x -= 1
        if head.y > tail.y:
            tail.y += 1
        else:
            tail.y -= 1

    tail.positions.add((tail.x, tail.y))
    return True


def move_command(inputCommand, head: Knot, tail: Knot, counter):
    splitted = inputCommand.split()
    steps = int(splitted[1])
    tailMoved = 0
    for i in range(steps):

        if splitted[0] == 'R':
            #print('move right')
            head.x += 1
        if splitted[0] == 'L':
            #print('move left')
            head.x -= 1
        if splitted[0] == 'U':
            #print('move up')
            head.y -= 1
        if splitted[0] == 'D':
            #print('move down')
            head.y += 1
        head.positions.add((head.x,head.y))
        distance = round(math.sqrt((head.x - tail.x) ** 2 + (head.y - tail.y) ** 2))
        if distance > 1:
            move_tail3(head, tail)

        #if 25 < counter < 50:
            #print()
            #draw_grid(head, tail)
            #if distance> 1:
                #print('tail moved')

    return tailMoved



def run_all_commands(lines, head: Knot, tail: Knot):
    moves = 0
    counter = 0
    for line in lines:
        moves += move_command(line, head, tail, counter)
        counter += 1
    return moves


def draw_grid(head: Knot, tail: Knot):
    for y in range(-15, 15):
        line = ""
        for x in range(-15, 15):

            if head.x == x and head.y == y:
                line += 'H'
            elif tail.x == x and tail.y == y:
                line += 'T'
            else:
                line += '.'
        print(line)


_head = Knot(0, 0)
_tail = Knot(0, 0)
_tail.positions.add((0,0))
_lines = read_file("sample.txt")
#print(lines)
moved = run_all_commands(_lines, _head, _tail)

print(len(_tail.positions))
