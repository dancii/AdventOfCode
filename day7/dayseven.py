import re

input_list = open('input.txt', 'r').read().split("\n")

class Program(object):
    name = ""
    parent = None
    children = []
    weight = 0

    def __init__(self, name, parent, children, weight):
        self.name = name
        self.parent = parent
        self.children = children
        self.weight = weight

def part_one():
    all_children_programs = []
    all_programs_with_children = []
    for program in input_list:
        if "->" in program:
            splited_program = program.split("->")
            all_programs_with_children.append(splited_program[0].split(" ")[0])
            all_children_programs.extend(splited_program[1].split(","))

    all_children_programs = [children.strip(' ') for children in all_children_programs]

    root = list(set(all_programs_with_children) - set(all_children_programs))
    print(root[0])

def find_parent(programs, child_name):
    for program in programs:
        if program.children is not None:
            if child_name in program.children:
                return program

def part_two():
    programs = []
    for program in input_list:
        all_children_programs = []
        weight = 0
        parent = None
        children = None
        if "->" in program:
            splited_program = program.split("->")
            parent_unparsed = splited_program[0]
            weight = int(parent_unparsed[parent_unparsed.find("(")+1:parent_unparsed.find(")")])
            all_children_programs.extend(splited_program[1].split(","))

            all_children_programs = [children.strip(' ') for children in all_children_programs]

            name = parent_unparsed.split(" ")[0]
            children = all_children_programs
            weight = weight
        else:
            name = program.split(" ")[0]
            weight_unparsed = program.split(" ")[1]
            weight = weight_unparsed[weight_unparsed.find("(")+1:weight_unparsed.find(")")]
        programs.append(Program(name, parent, children, weight))
        

    #loop, find all with children, find the children and add their parent, MAYBE NO NEED FOR THIS
    for program in programs:
        program.parent = find_parent(programs, program.name)
        
    root = None
    for program in programs:
        if program.parent is None:
            

part_two()