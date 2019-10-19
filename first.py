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
        return [0, 0]
    for key in keypad.keys():
        if c in keypad[key]:
            tap = keypad[key].index(c) + 1
            return [key, tap]


def smsTimer(p, w, text=''):
    time = 0
    temp = 0
    lastIndex = ''
    tempIndex = None
    tapSize = 0
    if text == '':
        return time

    for i in range(len(text)):
        temp = findingKey(text[i])
        print(temp)
        tempIndex = temp[0]
        tapSize = temp[1]
        if tempIndex != 1 and tempIndex == lastIndex:
            time += w
        lastIndex = tempIndex
        time += (tapSize * p)
        # Uncomment For Index Checking
        # print('This index is ' + str(tempIndex) +
        #       ' Last Index was ' + str(lastIndex))

    return time


testNumber = int(input('Enter Number Of Test Cases: '))


for i in range(testNumber):
    pAndW = (input('Enter p and w ')).split()
    p.append(int(pAndW[0]))
    w.append(int(pAndW[1]))
    print(p)
    print(w)
    text.append(input('Enter text ').upper())
    print(text)

for i in range(testNumber):
    print(smsTimer(p[i], w[i], text[i]))
