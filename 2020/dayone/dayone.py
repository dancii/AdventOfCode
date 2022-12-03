input = open('input.txt', 'r').read().split("\n")


def partone():
    for x in input:
        for y in input:
            if int(x)+int(y) == 2020:
                print(int(x)*int(y))
                break

def parttwo():
    for x in input:
        for y in input:
            for z in input:
                if int(x)+int(y)+int(z) == 2020:
                    print(int(x)*int(y)*int(z))
                    break

partone()
parttwo()