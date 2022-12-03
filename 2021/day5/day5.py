#!/usr/bin/python
inputs = open('input.txt').read().strip().split('\n')

from_coords = []
to_coords = []


for input in inputs:
    from_to_inputs = input.split(" -> ")
    from_coords.append(from_to_inputs[0])
    to_coords.append(from_to_inputs[1])

ground = [[0 for k in range(9)] for j in range(9)]

    
        

