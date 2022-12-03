input = open('/input.txt', 'r').read().split("\n")

def partOne():
    repeatSeq = []
    letters = []
    passwords = []

    validPasswords = 0

    for aTry in input:
        splittedTry = aTry.split(" ")
        repeatSeq.append(splittedTry[0])
        letters.append(splittedTry[1].replace(':', ''))
        passwords.append(splittedTry[2])

    for x in range(0, len(passwords)):
        splitRepeatSeq = repeatSeq[x].split("-")
        minRepeatSeq = int(splitRepeatSeq[0])
        maxRepeatSeq = int(splitRepeatSeq[1])

        countRepeatSeq = passwords[x].count(letters[x])

        if countRepeatSeq >= minRepeatSeq and countRepeatSeq <= maxRepeatSeq:
            validPasswords+=1
            
    print(validPasswords)

def partTwo():
    repeatSeq = []
    letters = []
    passwords = []

    validPasswords = 0

    for aTry in input:
        splittedTry = aTry.split(" ")
        repeatSeq.append(splittedTry[0])
        letters.append(splittedTry[1].replace(':', ''))
        passwords.append(splittedTry[2])

    for x in range(0, len(passwords)):
        splitRepeatSeq = repeatSeq[x].split("-")
        posOne = int(splitRepeatSeq[0])
        posTwo = int(splitRepeatSeq[1])

        if passwords[x][posOne-1] == letters[x] and passwords[x][posTwo-1] == letters[x]:
            continue
        elif passwords[x][posOne-1] == letters[x]:
            validPasswords+=1
        elif passwords[x][posTwo-1] == letters[x]:
            validPasswords+=1

            
    print(validPasswords)

partTwo()