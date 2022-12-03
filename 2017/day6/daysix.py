input_list = list(map(int, open('input.txt', 'r').read().split("\t")))

def distribute_max_value_from_block(index):
	block_count = input_list[index]
	input_list[index] = 0
	index += 1

	while block_count != 0:
		try:
			input_list[index] = int(input_list[index]) + 1
			block_count -= 1
			index += 1
		except IndexError:
			index = 0
			input_list[index] = int(input_list[index]) + 1
			block_count -= 1
			index += 1

def part_one():
	fingerprint_of_list = []
	cycles = 0
	while True:
		max_value = max(input_list)
		max_index = input_list.index(max_value)

		distribute_max_value_from_block(max_index)
		fingerprint_of_current_list = ''.join(map(str, input_list))
		cycles += 1
		try:
			if fingerprint_of_current_list in fingerprint_of_list:
				print(cycles)
				break
		except ValueError:
			pass
		fingerprint_of_list.append(fingerprint_of_current_list)

def part_two():
	fingerprint_of_list = []
	cycles = 0
	first_occurring_cycle_count = 0
	first_fingerprint_that_recurred = ""
	first_one_occured = False
	while True:
		max_value = max(input_list)
		max_index = input_list.index(max_value)

		distribute_max_value_from_block(max_index)
		fingerprint_of_current_list = ''.join(map(str, input_list))
		cycles += 1
		try:
			if fingerprint_of_current_list in fingerprint_of_list and first_one_occured == False:
				first_fingerprint_that_recurred = fingerprint_of_current_list
				first_occurring_cycle_count = cycles
				first_one_occured = True
			elif first_fingerprint_that_recurred == fingerprint_of_current_list:
				print(cycles-first_occurring_cycle_count)
				break
		except ValueError:
			pass
		fingerprint_of_list.append(fingerprint_of_current_list)

part_two()