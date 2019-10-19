keypad = {
    1: [' '],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
}


def findingKey(c):
    if c == '':
        return [0, 0]
    for key in keypad.keys():
        if c in keypad[key]:
            tab = keypad[key].index(c) + 1
            return [key, tab]


character = input('Enter Character: ').upper()
res = findingKey(character)

print(res)
