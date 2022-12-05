instructions = open('input.txt').read().strip().split('\n')

stacks_input = [['F', 'L', 'M', 'W'], ['F', 'M', 'V', 'Z', 'B'], ['Q', 'L', 'S', 'R', 'V', 'H'], ['J', 'T', 'M', 'P', 'Q', 'V', 'S', 'F'], ['W', 'S', 'L'], ['W', 'J', 'R', 'M', 'P', 'V', 'F'], ['F', 'R', 'N', 'P', 'C', 'Q', 'J'], ['B', 'R', 'W', 'Z', 'S', 'P', 'H', 'V'], ['W', 'Z', 'H', 'G', 'C', 'J', 'M', 'B']]

stacks_demo = [['N', 'Z'], ['D', 'C', 'M'], ['P']]

def extract_instructions(instruction):
    instruction_split = instruction.split(' ')
    count_to_move = int(instruction_split[1])
    move_from = int(instruction_split[3])-1
    move_to = int(instruction_split[5])-1
    return count_to_move, move_from, move_to

def part_one(stacks):

    for instruction in instructions:
        count_to_move, move_from, move_to = extract_instructions(instruction)
        for container in stacks[move_from][:count_to_move]:
            stacks[move_to].insert(0, container)
        stacks[move_from] = stacks[move_from][count_to_move:]

    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)

def part_two(stacks):

    for instruction in instructions:
        count_to_move, move_from, move_to = extract_instructions(instruction)
        stacks[move_to] = stacks[move_from][:count_to_move] + stacks[move_to]
        stacks[move_from] = stacks[move_from][count_to_move:]

    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)


part_two(stacks_input)