
def part_one(input):
    X = Y = input
    spiral_list = [[None]*X for i in range(Y)]
    x = y = 0
    dx = 0
    dy = -1
    startX = startY = 0
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            spiral_list[x][y] = i+1
            if (i+1) == 265149:
                startX = x
                startY = y
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    steps = abs(startX-0)+abs(startY-0)
    #print(spiral_list)
    print(steps)

def part_two(input):
    X = Y = int((input)**(1/2))
    spiral_list = [[0]*X for i in range(Y)]
    i = 1
    x = y = 0
    dx = 0
    dy = -1
    while True:
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            if i > 1:
                spiral_list[x][y] = check_around_for_neighbors_num(spiral_list,x,y,X,Y)
            else:
                spiral_list[x][y] = i
            if spiral_list[x][y] > 265149:
                print(spiral_list[x][y])
                break
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
        i+=1

def check_around_for_neighbors_num(spiral_list,x,y,X,Y):
    sum = 0
    #left
    if (-X/2 <= (x-1) <= X/2):
        left = spiral_list[x-1][y]
        if isinstance(left, int):
            sum += left
    #left diagonally
    if (-X/2 < (x-1) <= X/2) and (-Y/2 < y+1 <= Y/2):
        left_diagonally = spiral_list[x-1][y+1]
        if isinstance(left_diagonally, int):
            sum += left_diagonally
    #up
    if (-Y/2 < y+1 <= Y/2):
        up = spiral_list[x][y+1]
        if isinstance(up, int):
            sum += up
    #right diagonally
    if (-X/2 < (x+1) <= X/2) and (-Y/2 < y+1 <= Y/2):
        right_diagonally = spiral_list[x+1][y+1]
        if isinstance(right_diagonally, int):
            sum += right_diagonally
    #right
    if (-X/2 < (x+1) <= X/2):
        right = spiral_list[x+1][y]
        if isinstance(right, int):
            sum += right
    #down left diagonally
    if (-X/2 < (x-1) <= X/2) and (-Y/2 < y-1 <= Y/2):
        left_diagonally = spiral_list[x-1][y-1]
        if isinstance(left_diagonally, int):
            sum += left_diagonally
    #down
    if (-Y/2 < y-1 <= Y/2):
        up = spiral_list[x][y-1]
        if isinstance(up, int):
            sum += up
    #down right diagonally
    if (-X/2 < (x+1) <= X/2) and (-Y/2 < y-1 <= Y/2):
        right_diagonally = spiral_list[x+1][y-1]
        if isinstance(right_diagonally, int):
            sum += right_diagonally
    return sum
#part_one(515)

part_two(806)