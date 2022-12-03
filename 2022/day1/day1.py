input = open('input.txt').read().strip().split('\n\n')

calories_per_elf = []
for elf in input:
    calories_per_elf.append([eval(i) for i in elf.split("\n")])

def part_one(calories_per_elf):
    higher_calorie_elf = 0
    for elf in calories_per_elf:
        if sum(elf) > higher_calorie_elf:
            higher_calorie_elf = sum(elf)
    print(higher_calorie_elf)

def part_two(calories_per_elf):
    elf_1 = 0
    elf_2 = 0
    elf_3 = 0
    for elf_calories in calories_per_elf:
        sum_of_elf_calories = sum(elf_calories)
        if sum_of_elf_calories >= elf_1:
            elf_3 = elf_2
            elf_2 = elf_1
            elf_1 = sum_of_elf_calories
        elif sum_of_elf_calories >= elf_2:
            elf_3 = elf_2
            elf_2 = sum_of_elf_calories
        elif sum_of_elf_calories > elf_3:
            elf_3 = sum_of_elf_calories
            
    print(elf_1+elf_2+elf_3)

part_two(calories_per_elf)