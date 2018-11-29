import random, argparse, boto3

class SantaGenerator:
    def __init__(self, names):
        self.names = []
        for name in names:
            if name['name_entry'] is not None:
                self.names.append(name['name_entry'])
        self.assignments = self.assign_recipient(self.names)

    def get_names(self):
        return self.names

    def read_input_file(self, filename):
        return [line.rstrip('\n') for line in open(filename)]

    def assign_recipient(self, names):
        if len(names) == 0:
            return { "":"" }
        elif len(names) == 1:
            return {names[0]:names[0]}

        assignees = dict.fromkeys(names, None)
        for name in names:
            go_on = False
            while not go_on:
                to_assign_to = names[random.randint(0, len(names)-1)]
                if assignees[to_assign_to] != None or to_assign_to == name:
                    go_on = False
                else:
                    assignees[to_assign_to] = name
                    go_on = True
        return assignees


    def get_assigned(self):
        return self.assignments

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='path to files of names')
    parser.add_argument('filepath', type=str, help='path to name file')

    args = parser.parse_args()

    sg = SantaGenerator(args.filepath)
