def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


class Action:
    def __init__(self, chars, score, name):
        self.chars = chars
        self.score = score
        self.name = name
    win = {}


def match(other: Action, me: Action):
    if other.win == me:
        return 0
    if me.win == other:
        return 6
    return 3


def scoreFromTurn(other: Action, me: Action):
    score = gameResult(other, me)
    score += me.score
    return score


def gameResult(other: Action, me: Action):
    return match(other, me)


def has_all(chars, string):
    return any(string in s for s in chars)


def letterToAction(letter):
    letter = letter.lower()
    if has_all(rock.chars, letter):
        return rock
    if has_all(paper.chars, letter):
        return paper
    return scissor


def runGames(allLines):
    score = 0
    for l in allLines:
        split = l.split()
        other = letterToAction(split[0])
        me = letterToAction(split[1])
        matchScore = scoreFromTurn(other, me)
        score += matchScore
    return score


rock = Action(['a', 'x'], 1, 'rock')
paper = Action(['b', 'y'], 2, 'paper')
scissor = Action(['c', 'z'], 3, 'scissor')
rock.win = scissor
paper.win = rock
scissor.win = paper

lines = readFile('input.txt')

print(lines)
total = runGames(lines)
print(total)