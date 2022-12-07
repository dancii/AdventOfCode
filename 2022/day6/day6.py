datastream = open('input.txt').read()


def is_string_unique(partial_datastream):
    x=list(set(partial_datastream))
    y=list(partial_datastream)
    x.sort()
    y.sort()
    if(x==y):
        return True
    else:
        return False

def part_one():
    for i in range(0, len(datastream)):
        last_pos = i+4
        if is_string_unique(datastream[i:last_pos]):
            print(last_pos)
            break

def part_two():
    for i in range(0, len(datastream)):
        last_pos = i+14
        if is_string_unique(datastream[i:last_pos]):
            print(last_pos)
            break
    
part_two()