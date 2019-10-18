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
        # Uncomment For Index Checking
        # print('This index is ' + str(tempIndex) +
        #       ' Last Index was ' + str(lastIndex))

    return time


testNumber = int(input('Enter Number Of Test Cases: '))


for i in range(testNumber):
    p.append(int(input('Enter p ')))
    w.append(int(input('Enter w ')))
    text.append(input('Enter text ').upper())

for i in range(testNumber):
    print(smsTimer(p[i], w[i], text[i]))
