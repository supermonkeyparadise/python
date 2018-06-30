from user import User
import json

# [ csv format ]
# user = User('Steven')
#
# user.add_movie('The Matrix', 'Sci-Fi')
# user.add_movie('The Interview', 'Comedy')
#
# user.save_to_file()
# user = User.load_from_file('Steven.txt')
#
# print(user.name)
# print(user.movies)


# [ Write the Json format to the file ]
# user = User('Steven')
#
# user.add_movie('The Matrix', 'Sci-Fi')
# user.add_movie('The Interview', 'Comedy')
#
# with open('my_file.txt', 'w') as f:
#     json.dump(user.json(), f)

# [ Load the Json format to the file ]
with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json())