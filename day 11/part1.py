def read_file(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


class Monkey:
    def __init__(self, starting, number, operation, divisible, true, false):
        self.items = starting
        self.number = number
        self.operation = operation
        self.test = divisible
        self.true = true
        self.false = false
        self.inspections = 0


class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level
        self.starting_value = worry_level


def create_monkey_from_line(monkey_line):
    splitted = monkey_line.split('|')
    number = splitted[0].split()[1][:-1]
    items = []
    item_list = splitted[1].split(':')[1].split(',')
    for item in item_list:
        it = Item(int(item))
        items.append(it)
    operation = splitted[2].split('=')[1]
    test = splitted[3].split('by')[1]
    true = splitted[4].split('monkey')[1]
    false = splitted[5].split('monkey')[1]
    return Monkey(items,  int(number),operation,int(test),int(true),int(false))


def get_monkey_list(lines):
    monkeys = []
    monkey_line=''
    for i in range(len(lines)):
        if lines[i] == '':
            monkey = create_monkey_from_line(monkey_line[:-1])
            monkeys.append(monkey)
            monkey_line = ''
            continue
        monkey_line += lines[i]+'|'

    monkey = create_monkey_from_line(monkey_line[:-1])
    monkeys.append(monkey)
    return monkeys


def print_monkey_items(items):
    item_string = ''
    for item in items:
        item_string += str(item.worry_level) + ','
    return item_string[:-1]


def print_monkey(monkey: Monkey):
    print('monkey no: ' + str(monkey.number))
    print('items: ' + print_monkey_items(monkey.items))
    print('operation: ' + monkey.operation)
    print('test divisible by: ' + str(monkey.test))
    print('if true: ' + str(monkey.true))
    print('if false: ' + str(monkey.false))
    print('inspections: ' + str(monkey.inspections))


def print_monkeys(monkeys):
    for monkey in monkeys:
        print_monkey(monkey)
        print()


def give_item_from_to(monkey_from, item, monkey_to):
    monkey_from.items.remove(item)
    monkey_to.items.append(item)


def monkey_update_worry_level(monkey_from, item):
    splitted = monkey_from.operation.strip().split('old')
    op = splitted[1].strip().split()
    value = item.worry_level
    if len(op) == 2:
        value = int(op[1])
    if op[0] == '+':
        item.worry_level = int(item.worry_level + value)
    elif op[0] == '*':
        item.worry_level = int(item.worry_level * value)


def monkey_pass_test_item(monkey_from, item):
    result = item.worry_level % monkey_from.test == 0
    return result


def monkey_bored(item):
    item.worry_level = int(item.worry_level / 3)


def play_round(monkeys):
    for monkey in monkeys:
        item_action_list = []
        for item in monkey.items:
            monkey.inspections += 1
            monkey_update_worry_level(monkey, item)
            monkey_bored(item)
            test_result = monkey_pass_test_item(monkey, item)
            if test_result:
                item_action_list.append((item, monkey.true))
            else:
                item_action_list.append((item, monkey.false))

        for item in item_action_list:
            give_item_from_to(monkey, item[0], monkeys[int(item[1])])


def play_rounds(rounds):
    for i in range(rounds):
        play_round(_monkeys)


def find_top_two(monkeys):
    top = []
    while len(top) != 2:
        top_monkey = Monkey([], -1, '', 0, 0, 0)
        for monkey in monkeys:
            if monkey.inspections > top_monkey.inspections:
                top_monkey = monkey
        top.append(top_monkey)
        monkeys.remove(top_monkey)
    return top


_lines = read_file("input.txt")
print(_lines)
_monkeys = get_monkey_list(_lines)
#print_monkeys(_monkeys)
play_rounds(20)
#print_monkeys(_monkeys)
_top_two = find_top_two(_monkeys)
print(_top_two[0].inspections*_top_two[1].inspections)



