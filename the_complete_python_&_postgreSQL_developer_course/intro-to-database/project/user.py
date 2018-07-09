from database import ConnectionPool


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def save_to_db(self):
        # connection = psycopg2.connect(user='postgres', password='root1224', database='learning', host='localhost')
        # with connection.cursor() as cursor:
        #     cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
        #                    (self.email,
        #                     self.first_name,
        #                     self.last_name))
        #
        # connection.commit()
        # connection.close()

        # auto commit
        # with connection_pool.getconn() as connection:
        #     with connection.cursor() as cursor:
        #         cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
        #                        (self.email,
        #                         self.first_name,
        #                         self.last_name))

        with ConnectionPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                               (self.email,
                                self.first_name,
                                self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with ConnectionPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM users WHERE email=%s', (email,))  # (123, '456') == [123, '456']
                user_data = cursor.fetchone()
                return cls(user_data[1], user_data[2], user_data[3], user_data[0])
