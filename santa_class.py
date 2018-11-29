import random, argparse, boto3, re

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


class MessageSender:
    def __init__(self, names, number_dict):
        num_list = []
        for entry in number_dict:
            if entry['phone_number'] is not None:
                num_list.append(str(entry['phone_number'].national_number))
        self.valid_nums = self.validate_numbers(num_list)
        self.user_dict = self.make_dict(names, self.valid_nums) #{user: number}

    def make_dict(self, names, numbers):
        users = {}
        for i in range(len(numbers)):
            users[names[i]] = numbers[i]
        return users

    def get_valid_nums(self):
        return self.valid_nums

    def separate_numbers(self, numbers):
        return [x.strip() for x in numbers.split(',')]

    def validate_numbers(self, numbers):
        num_regex = re.compile("\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}")
        validated_nums = []
        for number in numbers:
            if not num_regex.match(number):
                validated_nums.append('INVALID')
            else:
                number_fixed = number.replace("(", "").replace(")", "").replace(" ", "-").replace(".", "")
                validated_nums.append(number_fixed)

        return validated_nums

    def send_texts(self, assignments):
        sns = boto3.client('sns', region_name="us-east-1")
        i = 0
        for user in self.user_dict:
            my_assgn = assignments[user]
            message = "You (%s) are assigned to gift to: %s!" %(user, my_assgn)
            my_number = "+1" + self.user_dict[user]
            sns.publish(PhoneNumber = my_number, Message=message)
        return self.user_dict
