from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            database='learning',
                                            user='postgres',
                                            password='root1224',
                                            host='localhost')


class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    # for with clause
    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection  # connection has attribute 'cursor'

    # for with clause
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        connection_pool.putconn(self.connection)
