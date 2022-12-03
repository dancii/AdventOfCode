#!/usr/bin/python
inputs = open('input.txt').read().strip().split('\n')

def part_one():
    gama_rate = [0] * 12
    epsilon_rate = [0] * 12
    for input in inputs:
        for index, bit in enumerate(input):
            if int(bit) == 0:
                gama_rate[index] -= 1
            else:
                gama_rate[index] += 1
    for index, bit in enumerate(gama_rate):
        if bit > 0:
            gama_rate[index] = "1"
            epsilon_rate[index] = "0"
        else:
            gama_rate[index] = "0"
            epsilon_rate[index] = "1"
    
    print(int("".join(gama_rate), 2) * int("".join(epsilon_rate), 2))

def part_two():
    #print(O2_gen_rating(0, inputs))
    print(int("".join(O2_gen_rating(0, inputs)), 2) * int("".join(CO2_scrub_rating(0, inputs)), 2))


def O2_gen_rating(index, possibilities):
    if len(possibilities) == 1:
        print("O2:"+"".join(possibilities))
        return possibilities
    
    majority_bit = 0
    for byte in possibilities:
        if (int(byte[index])) == 0:
            majority_bit -= 1
        else:
            majority_bit += 1

    O2_gen_rating_possibilities = []
    for byte in possibilities:
        if majority_bit > 0 and int(byte[index]) == 1:
            O2_gen_rating_possibilities.append(byte)
        elif majority_bit < 0 and int(byte[index]) == 0:
            O2_gen_rating_possibilities.append(byte)
        elif majority_bit == 0 and int(byte[index]) == 1:
            O2_gen_rating_possibilities.append(byte)

    index += 1

    return O2_gen_rating(index, O2_gen_rating_possibilities)

def CO2_scrub_rating(index, possibilities):
    if len(possibilities) == 1:
        print("CO2:"+"".join(possibilities))
        return possibilities
    
    majority_bit = 0
    for byte in possibilities:
        if (int(byte[index])) == 0:
            majority_bit -= 1
        else:
            majority_bit += 1
    
    CO2_scrub_rating_possibilities = []
    for byte in possibilities:
        if majority_bit > 0 and int(byte[index]) == 0:
            CO2_scrub_rating_possibilities.append(byte)
        elif majority_bit < 0 and int(byte[index]) == 1:
            CO2_scrub_rating_possibilities.append(byte)
        elif majority_bit == 0 and int(byte[index]) == 0:
            CO2_scrub_rating_possibilities.append(byte)

    index += 1

    return CO2_scrub_rating(index, CO2_scrub_rating_possibilities)

part_two()