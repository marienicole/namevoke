import random

def read_input_file(filename):
    return [line.rstrip('\n') for line in open(filename)]


def assign_recipient(names):
    assignees = dict.fromkeys(names, None)
    for name in names:
        go_on = False
        while not go_on:
            rand = random.randint(0, len(names)-1)
            to_assign_to = names[rand]
            if assignees[to_assign_to] != None or to_assign_to == name:
                go_on = False
            else:
                assignees[to_assign_to] = name
                go_on = True

    print(assignees)


def output_assigned_list():
    pass

names = read_input_file('../names.txt')
assign_recipient(names)
