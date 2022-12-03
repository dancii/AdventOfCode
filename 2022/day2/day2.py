games = open('input.txt').read().strip().split('\n')

def part_one():
    game_score = 0
    for game in games:
        game_score += game_score_calculation(game)
    print (game_score)

def part_two():
    game_score = 0
    for game in games:
        game_score += game_score_calculation_2(game)
    print(game_score)

def game_score_calculation(game):
    if i_won(game[0], game[2]):
        return score_addition("WON", game[2])
    elif draw(game[0], game[2]):
        return score_addition("DRAW", game[2])
    else:
        return score_addition("LOST", game[2])

def i_won(opponent, me):
    if me == 'X' and opponent == 'C':
        return True
    elif me == 'Z' and opponent == 'B':
        return True
    elif me == 'Y' and opponent == 'A':
        return True

def draw(opponent, me):
    if me == 'X' and opponent == 'A':
        return True
    elif me == 'Y' and opponent == 'B':
        return True
    elif me == 'Z' and opponent == 'C':
        return True

def game_score_calculation_2(game):
    if game[2] == 'Z':
        return score_addition("WON", hand_i_played_to_win(game[0]))
    elif game[2] == 'Y':
        return score_addition("DRAW", hand_i_played_to_draw(game[0]))
    else:
        return score_addition("LOST", hand_i_played_to_lose(game[0]))

def hand_i_played_to_win(opponent):
    if opponent == 'C':
        return 'X'
    elif opponent == 'B':
        return 'Z'
    elif opponent == 'A':
        return 'Y'

def hand_i_played_to_draw(opponent):
    if opponent == 'A':
        return 'X'
    elif opponent == 'C':
        return 'Z'
    elif opponent == 'B':
        return 'Y'

def hand_i_played_to_lose(opponent):
    if opponent == 'C':
        return 'Y'
    elif opponent == 'B':
        return 'X'
    elif opponent == 'A':
        return 'Z'

def score_addition(game_state, my_hand):
    score = 0
    if game_state == "WON":
        score += 6
    elif game_state == "DRAW":
        score += 3
    elif game_state == "LOST":
        score += 0
    
    if my_hand == 'X':
        score += 1
    elif my_hand == 'Y':
        score += 2
    elif my_hand == 'Z':
        score += 3
    return score

part_two()
