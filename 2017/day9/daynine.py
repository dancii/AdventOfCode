stream = list(open('input.txt', 'r').read())

score = 0
deep = 1
in_garbage = False
skip_next = False
count_in_garbage = 0
for character in stream:
    if in_garbage == False:
        if character == "<":
            in_garbage = True
        elif character == "{":
            score += deep
            deep+=1
        elif character == "}":
            deep-=1
    else:
        count_in_garbage+=1
        if skip_next:
            skip_next = False
            count_in_garbage-=1
            continue
        if character == ">":
            count_in_garbage-=1
            in_garbage = False
        elif character == "!":
            count_in_garbage-=1
            skip_next = True
            continue

print(score)
print(count_in_garbage)
