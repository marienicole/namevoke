from flask import Flask
import random, argparse

class SantaGenerator:
    def __init__(self, namefile):
        self.names = self.read_input_file(namefile)
        assignments = self.assign_recipient(self.names)
        print(assignments)

    def read_input_file(self, filename):
        return [line.rstrip('\n') for line in open(filename)]


    def assign_recipient(self, names):
        if len(names) in [0, 1]:
            return names

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


    def output_assigned_list(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='path to files of names')
    parser.add_argument('filepath', type=str, help='path to name file')

    args = parser.parse_args()

    sg = SantaGenerator(args.filepath)
