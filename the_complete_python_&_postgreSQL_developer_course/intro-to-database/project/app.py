from user import User

# CALL User class __init__
my_user = User('alex@gmail.com', 'Alex', 'Hung', None)

my_user.save_to_db()


# my_user = User.load_from_db_by_email('steven.chou@gmail.com')
# print(my_user)
