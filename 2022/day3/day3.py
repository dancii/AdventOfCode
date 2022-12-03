backpacks = open('input.txt').read().strip().split('\n')

letters = [chr(i) for i in range(97, 123)]
for i in range(65, 91):
    letters.append(chr(i))
prio_score = dict(zip(letters, range(1,53)))

def split_backpack(backpack):
    n = len(backpack)
    half = int(n/2)
    return backpack[:half], backpack[n-half:]

def part_one():
    sum_of_prio = 0
    for backpack in backpacks:
        container_a, container_b = split_backpack(backpack)

        for char in container_a:
            if char in container_b:
                sum_of_prio += prio_score.get(char)
                break
    print(sum_of_prio)

def part_two(backpacks):
    sum_of_prio = 0
    n = 3
    group_of_three = [backpacks[i:i+n] for i in range(0, len(backpacks), n)]
    
    for group_of_backpacks in group_of_three:
        for char in group_of_backpacks[0]:
            if char in group_of_backpacks[1] and char in group_of_backpacks[2]:
                sum_of_prio += prio_score.get(char)
                break
    print(sum_of_prio)
    
                
part_two(backpacks)