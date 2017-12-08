raw_instructions = open('input.txt', 'r').read().split("\n")

variables = {}
highest_value_ever = 0

def split_condition(math_exp, condition):
		splited_condition = condition.split(math_exp)
		variable = splited_condition[0]
		num = int(splited_condition[1])
		return variable, num

def does_condition_pass(condition):
	if "==" in condition:
		variable, num = split_condition("==", condition)
		if variables[variable] == num:
			return True
	elif ">=" in condition:
		variable, num = split_condition(">=", condition)
		if variables[variable] >= num:
			return True
	elif "<=" in condition:
		variable, num = split_condition("<=", condition)
		if variables[variable] <= num:
			return True
	elif ">" in condition:
		variable, num = split_condition(">", condition)
		if variables[variable] > num:
			return True
	elif "<" in condition:
		variable, num = split_condition("<", condition)
		if variables[variable] < num:
			return True
	elif "!=" in condition:
		variable, num = split_condition("!=", condition)
		if variables[variable] != num:
			return True
	return False


for raw_instruction in raw_instructions:
	splited_raw_instruction = raw_instruction.split("if")
	instruction = splited_raw_instruction[0].replace(' ', '')

	variable = ""

	if "inc" in instruction:
		splited_instruction = instruction.split("inc")
		variable = splited_instruction[0]
	else:
		splited_instruction = instruction.split("dec")
		variable = splited_instruction[0]

	variables[variable] = 0

for raw_instruction in raw_instructions:
	splited_raw_instruction = raw_instruction.split("if")
	instruction = splited_raw_instruction[0].replace(' ', '')
	condition = splited_raw_instruction[1].replace(' ', '')

	if "inc" in instruction:
		splited_instruction = instruction.split("inc")
		variable = splited_instruction[0]
		numb = int(splited_instruction[1])
		
		if does_condition_pass(condition):
			variables[variable] = variables[variable] + numb

		if variables[variable] > highest_value_ever:
			highest_value_ever = variables[variable]

	else:
		splited_instruction = instruction.split("dec")
		variable = splited_instruction[0]
		numb = int(splited_instruction[1])
		
		if does_condition_pass(condition):
			variables[variable] = variables[variable] - numb

		if variables[variable] > highest_value_ever:
			highest_value_ever = variables[variable]


print("Part one: "+str(variables[max(variables, key=variables.get)]))
print("Part two: "+str(highest_value_ever))
