import random

minimum = 100

for index in range(10):
    random_number = random.randint(0, 100)
    print('The number generated is {}'.format(random_number))

    if random_number <= minimum:
        minimum = random_number

print(minimum)
