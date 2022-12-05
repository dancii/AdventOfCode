assignments = open('input.txt').read().strip().split('\n')    

def is_overlap(interval_1, interval_2):
    if int(interval_1[0]) <= int(interval_2[0]) and int(interval_1[1]) >= int(interval_2[1]):
        return True
    elif int(interval_1[0]) >= int(interval_2[0]) and int(interval_1[1]) <= int(interval_2[1]):
        return True
    else:
        return False

def is_inside_range(interval_1, interval_2):
    if int(interval_1[0]) > int(interval_2[1]) or int(interval_1[1]) < int(interval_2[0]):
        return False
    else:
        return True

def part_one():
    assignment_overlap_range_count = 0
    for assignment in assignments:
        elf_1, elf_2 = assignment.split(',')
        if is_overlap(elf_1.split('-'), elf_2.split('-')):
            assignment_overlap_range_count += 1
    
    print(assignment_overlap_range_count)

def part_two():
    assignment_inside_range_count = 0
    for assignment in assignments:
        elf_1, elf_2 = assignment.split(',')
        if is_inside_range(elf_1.split('-'), elf_2.split('-')):
            assignment_inside_range_count += 1
    
    print(assignment_inside_range_count)

part_two()