from database import Database
from user import User

Database.initialise(database='learning',
                    user='postgres',
                    password='root1224',
                    host='localhost')

# CALL User class __init__
my_user = User('jean.lin@gmail.com', 'Jean', 'Lin', None)

my_user.save_to_db()

my_user = User.load_from_db_by_email('jean.lin@gmail.com')

print(my_user)
