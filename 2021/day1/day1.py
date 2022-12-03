#!/usr/bin/python
depth_measurements = open('input.txt').read().strip().split('\n')

def part_one():
    inc = 0

    for depth, nextDepth in zip(depth_measurements, depth_measurements[1:]):
        if (int(nextDepth) > int(depth)):
            inc += 1
            print(nextDepth+" is bigger than "+depth)
        else:
            print(nextDepth+" is smaller than "+depth)

    print(inc)

def part_two():
    previous = 0
    current = 0
    inc = 0

    for depth_one, depth_two, depth_three in zip(depth_measurements, depth_measurements[1:], depth_measurements[2:]):
        current = int(depth_one) + int(depth_two) + int(depth_three)
        print("Current: "+str(current)+"    "+depth_one+", "+depth_two+", "+depth_three)
        
        if previous != 0 and current > previous:
            print("Current: "+str(current)+" Previous: "+str(previous))
            inc += 1
        previous = current

    print(inc)

part_two()