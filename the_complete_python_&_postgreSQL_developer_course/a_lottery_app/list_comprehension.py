user_input = '5,4,25,18,22,9'
user_numbers = user_input.split(',')

user_numbers_as_int = []
for number in user_numbers:
    user_numbers_as_int.append(int(number))

print(user_numbers_as_int)

print([number for number in user_numbers])

print([number*2 for number in user_numbers])

print([int(number) for number in user_numbers])
