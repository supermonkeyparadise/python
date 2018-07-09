from psycopg2 import pool


class Database:
    connection_pool = None  # class member

    # @staticmethod
    # def initialise():
    #     Database.connection_pool = pool.SimpleConnectionPool(1,
    #                                                          10,
    #                                                          database='learning',
    #                                                          user='postgres',
    #                                                          password='root1224',
    #                                                          host='localhost')

    @classmethod
    def initialise(cls):
        cls.connection_pool = pool.SimpleConnectionPool(1,
                                                        10,
                                                        database='learning',
                                                        user='postgres',
                                                        password='root1224',
                                                        host='localhost')

    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        cls.connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        cls.connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    # for with clause
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    # for with clause
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()

        Database.return_connection(self.connection)
