input = open('input.txt', 'r').read().replace("\n", "")


def partone():
    sum = 0

    if input[0] == input[len(input)-1]:
            sum+=int(input[0])

    for x in range(0, len(input)-1):
        if input[x] == input[x+1]:
            sum+=int(input[x])

    print(sum)

def parttwo():
    sum = 0

    steps = int(len(input)/2)
    
    for x in range(0, len(input)):
        if x+steps > len(input)-1:
            temp = steps - ((len(input)-1) - x)
            if input[x] == input[temp - 1]:
                sum+=int(input[x])
        elif input[x] == input[x+steps]:
                sum+=int(input[x])
    print(sum)

partone()
parttwo()