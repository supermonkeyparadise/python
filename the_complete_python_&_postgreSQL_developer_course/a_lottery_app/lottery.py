import random


def get_player_numbers():
    number_csv = input('Enter your 6 numbers, separated by commas:')
    number_list = number_csv.split(',')
    integer_set = {int(number) for number in number_list}

    return integer_set


def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))

    return values


print(get_player_numbers())
print(create_lottery_numbers())
