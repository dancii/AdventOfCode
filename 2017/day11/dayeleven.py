import math

instructions = open("input.txt", "r").read().split(",")

coords = [0,0,0]

def direction_to_steps(direction):
	if direction == "n":
		return [0,1,-1]
	elif direction == "ne":
		return [1,0,-1]
	elif direction == "se":
		return [1,-1,0]
	elif direction == "s":
		return [0,-1,1]
	elif direction == "sw":
		return [-1,0,1]
	elif direction == "nw":
		return [-1,1,0]

def calculate_shortest_path(final_coords):
	x = abs(final_coords[0])
	y = abs(final_coords[1])
	z = abs(final_coords[2])

	return (abs(x)+abs(y)+abs(z))/2

longest_path = 0

for direction in instructions:
	temp = direction_to_steps(direction)

	coords[0]+=temp[0]
	coords[1]+=temp[1]
	coords[2]+=temp[2]

	steps = calculate_shortest_path(coords)

	if steps > longest_path:
		longest_path = steps

print(calculate_shortest_path(coords))
print(longest_path)