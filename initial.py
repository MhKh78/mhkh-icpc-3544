p = []
w = []
text = []
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
        return 0
    for key in keypad.keys():
        if c in keypad[key]:
            return key


def smsTimer(p, w, text=''):
    time = 0
    lastIndex = ''
    tempIndex = ''
    if text == '':
        return time

    textLenght = len(text)
    for i in range(textLenght):
        tempIndex = findingKey(text[i])
        if tempIndex != 1 and tempIndex == lastIndex:
            time += w
        lastIndex = tempIndex
        time += p

    return time


testNumber = int(input())


for i in range(testNumber):
    p.append(int(input()))
    w.append(int(input()))
    text.append(input().upper())

for i in range(testNumber):
    print(smsTimer(p[i], w[i], text[i]))
