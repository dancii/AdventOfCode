input = open('input.txt', 'r').read().replace("\t", ",").split("\n")

def part_one():
    checksum = 0
    for x in input:
        strList = x.split(",")
        if len(strList) > 1:
            intList = list(map(int, strList))
            checksum += max(intList) - min(intList)

    print(checksum)

def part_two():
    checksum = 0
    for x in input:
        strList = x.split(",")
        if len(strList) > 1:
            intList = list(map(int, strList))
            print(intList)
            for i in range(0, len(intList)):
                for num in intList:
                    if intList[i] != num:
                        if intList[i] % num == 0:
                            checksum+=(intList[i]/num)

    print(checksum)

part_two()