import boto3, re

class MessageSender:
    def __init__(self, names, num_str):
        #self.client = boto3.client('sns')
        print("num str:")
        print(num_str)
        num_list = self.separate_numbers(num_str)
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
                validated_nums.append(number)

        return validated_nums

    def send_texts(self, assignments):
        sns = boto3.client('sns')
        i = 0
        for user in self.user_dict:
            my_assgn = assignments[user]
            message = "You (%s) are assigned to gift to: %s!" %(user, my_assn)
            sns.publish(PhoneNumber = self.user_dict[user], Message=message)
        return("Messages sent successfully!")
