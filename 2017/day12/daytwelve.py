pipes_input = open("input.txt", "r").read().split("\n")

programs = []
list_with_ways = []

group_members = set()

for pipes in pipes_input:
	pipes_splited = pipes.replace(" ","").split("<->")
	programs.append(pipes_splited[1])

def search(programs_temp):
	temp = programs_temp.split(",")
	for program in temp:
		if int(program) in group_members:
			continue
		group_members.add(int(program))
		try:
			search(programs[int(program)])
		except ValueError:
			continue

def part_one():
	search(programs[0])
	print(len(group_members))

def part_two():

	groups = 0

	for x in range(0,2000):
		if x not in group_members:
			search(programs[x])
			groups+=1

	print(groups)

part_two()