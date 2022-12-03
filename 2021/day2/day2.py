#!/usr/bin/python
inputs = open('input.txt').read().strip().split('\n')

def part_one():
    h_pos = 0
    d_pos = 0
    for input in inputs:
        command = input.split(" ")
        if "forward" in command[0]:
            h_pos += int(command[1])
        elif "up" in command[0]:
            d_pos -= int(command[1])
        elif "down" in command[0]:
            d_pos += int(command[1])

    print(d_pos * h_pos)

def part_two():
    h_pos = 0
    d_pos = 0
    aim = 0
    for input in inputs:
        command = input.split(" ")
        if "forward" in command[0]:
            h_pos += int(command[1])
            d_pos += aim * int(command[1])
        elif "up" in command[0]:
            aim -= int(command[1])
        elif "down" in command[0]:
            aim += int(command[1])

    print(d_pos * h_pos)
part_two()