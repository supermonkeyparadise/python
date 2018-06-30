from user import User

# user.save_to_file()
user = User.load_from_file('Steven.txt')

print(user.name)
print(user.movies)
