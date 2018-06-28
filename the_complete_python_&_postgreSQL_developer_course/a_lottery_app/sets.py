# empty set
numbers = set()
numbers.add(3)
numbers.add(3)

print(numbers)

# set with no order and unique value
lottery_values = {2, 4, 18, 8}
print(lottery_values)
user_values = {1, 2, 3, 4}
print(user_values)

# 交集
print(lottery_values.intersection(user_values))
print(user_values.intersection(lottery_values))
