import random


def get_player_numbers():
    number_csv = input('Enter your 6 numbers, separated by commas:')
    number_list = number_csv.split(',')
    integer_set = {int(number) for number in number_list}

    return integer_set


print(get_player_numbers())
