import binascii
from functools import reduce
from operator import xor

input_list = list(map(int,open('input.txt', 'r').read().split(',')))
input_string = list(open('input.txt', 'r').read())

numbers = [x for x in range(256)]

def part_one():
    list_len = len(numbers)
    current_pos = 0
    skip_size = 0
    for len_jump in input_list:
        y = len_jump + current_pos
        if y > list_len:
            
            y = y % list_len

            temp = (numbers[current_pos:list_len]+numbers[0:y])[::-1]

            numbers[current_pos:list_len] = temp[0:((list_len-current_pos))]
            
            numbers[0:y] = temp[(list_len-current_pos):list_len]
            
        else:
            numbers[current_pos:current_pos+len_jump] = numbers[current_pos:current_pos+len_jump][::-1]
        current_pos=(current_pos+len_jump+skip_size) % list_len
        skip_size+=1
    print(numbers[0]*numbers[1])

def part_two():
    end_ascii_chars = [17,31,73,47,23]
    ascii_string = [ord(c) for c in input_string]
    ascii_string = ascii_string+end_ascii_chars

    list_len = len(numbers)
    current_pos = 0
    skip_size = 0

    for _ in range(64):
        for ascii_char in ascii_string:
            y = ascii_char + current_pos
            if y > list_len:
                
                y = y % list_len

                temp = (numbers[current_pos:list_len]+numbers[0:y])[::-1]

                numbers[current_pos:list_len] = temp[0:((list_len-current_pos))]
                
                numbers[0:y] = temp[(list_len-current_pos):list_len]
                
            else:
                numbers[current_pos:current_pos+ascii_char] = numbers[current_pos:current_pos+ascii_char][::-1]
            current_pos=(current_pos+ascii_char+skip_size) % list_len
            skip_size+=1

    dense = []
    for x in range(16,257,16):
        subslice = numbers[(x-16):x]
        dense.append('%02x'%reduce(xor,subslice))
        print(dense)
    print(''.join(dense))

part_two()