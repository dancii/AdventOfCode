#!/usr/bin/python
inputs = open('input.txt').read().strip().split('\n')

draw_numbers = inputs.pop(0).split(",")
boards = []
inputs.pop(0)
board = []

for input in inputs:
    if input == '':
        boards.append(board)
        board = []
        continue
    row = input.split(" ")
    while True:
        try:
            row.remove("")
        except ValueError:
            break
    board.append(row)
boards.append(board)

bingo_boards = [[[0 for k in range(5)] for j in range(5)] for i in range(len(boards))]

def part_one():
    for drawn_number in draw_numbers:
        for index, board in enumerate(boards):
            for x in range(0, 5):
                for y in range(0, 5):
                    if board[x][y] == drawn_number:
                        bingo_boards[index][x][y] = 1
                        winner_bingo_board_index = is_bingo(bingo_boards)
                        if winner_bingo_board_index is not -1:
                            calculate_final_score(boards[winner_bingo_board_index], bingo_boards[winner_bingo_board_index], drawn_number)
                            return

def part_two():
    for drawn_number in draw_numbers:
        for index, board in enumerate(boards):
            for x in range(0, 5):
                for y in range(0, 5):
                    if board[x][y] == drawn_number:
                        bingo_boards[index][x][y] = 1
                        if does_all_board_have_bingo(bingo_boards):
                            calculate_final_score(boards[index], bingo_boards[index], drawn_number)
                            return
                            
    
def is_bingo(bingo_boards):
    for index, bingo_board in enumerate(bingo_boards):
        for row in bingo_board:
            if sum(row) == 5:
                return index
        for i in range(0, 5):
            if sum(column(bingo_board, i)) == 5:
                return index
    return -1

def does_all_board_have_bingo(bingo_boards):
    records_of_boards_had_bingo = [0 for k in range(len(boards))]

    for index, bingo_board in enumerate(bingo_boards):
        for row in bingo_board:
            if sum(row) == 5:
                records_of_boards_had_bingo[index] = 1
        for i in range(0, 5):
            if sum(column(bingo_board, i)) == 5:
                records_of_boards_had_bingo[index] = 1
        if sum(records_of_boards_had_bingo) == len(bingo_boards):
            return True
    return False
    
def column(matrix, i):
    return [row[i] for row in matrix]

def calculate_final_score(board, bingo_mark_board, bingo_drawn_number):
    sum_of_unmarked = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if bingo_mark_board[x][y] == 0:
                sum_of_unmarked += int(board[x][y])
    print(sum_of_unmarked * int(bingo_drawn_number))

part_two()