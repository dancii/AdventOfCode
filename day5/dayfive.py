input_list = open('input.txt', 'r').read().split("\n")

def part_one():
	jump = 0
	total_jumps = 0

	while True:
		try:
			oldJump = jump
			jump+=int(input_list[jump])
			input_list[oldJump] = int(input_list[oldJump]) + 1
			total_jumps+=1
		except IndexError:
			print(total_jumps)
			break

def part_two():
	jump = 0
	total_jumps = 0

	while True:
		try:
			oldJump = jump
			jump+=int(input_list[jump])
			if int(input_list[oldJump]) >= 3:
				input_list[oldJump] = int(input_list[oldJump]) - 1
			else:
				input_list[oldJump] = int(input_list[oldJump]) + 1
			total_jumps+=1
		except IndexError:
			print(total_jumps)
			break