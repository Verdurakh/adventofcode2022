import math


def read_file(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


class Knot:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.positions = set()
        self.positions.add((x, y))
        self.isHead = False
        self.char = char


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


def move_command(inputCommand, head: Knot, tails):
    splitted = inputCommand.split()
    steps = int(splitted[1])
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
        head.positions.add((head.x, head.y))
        i = 1
        for ntail in tails:
            if ntail.isHead:
                continue
            nhead = tails[i-1]
            distance = round(math.sqrt((nhead.x - ntail.x) ** 2 + (nhead.y - ntail.y) ** 2))
            if distance > 1:
                move_tail3(nhead, ntail)
            i += 1

        #if 0 < counter < 50:
        #print()
        #draw_grid(head, tails)
        #if distance> 1:
            #print('tail moved')


def run_all_commands(lines, head: Knot, tail):
    for line in lines:
        move_command(line, head, tail)


def draw_grid(head: Knot, tails):
    for y in range(-15, 15):
        line = ""
        for x in range(-15, 15):
            added = False
            for tail in tails:
                if tail.x == x and tail.y == y:
                    added = True
                    line += tail.char
                    break
            if not added:
                line += '.'

        print(line)


_head = Knot(0, 0, 'H')
_head.isHead = True
_rope = [_head]
for i in range(9):
    __knot = Knot(0, 0, str(i))
    _rope.append(__knot)
_lines = read_file("input.txt")
#print(lines)
#print('starting pos')
#draw_grid(_head, _rope)
#print('run commands')
run_all_commands(_lines, _head, _rope)
#print('finished')
print(len(_rope[9].positions))
