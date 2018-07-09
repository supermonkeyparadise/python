from psycopg2 import pool


class ConnectionPool:
    def __init__(self):
        self.connection_pool = pool.SimpleConnectionPool(1,
                                                         10,
                                                         database='learning',
                                                         user='postgres',
                                                         password='root1224',
                                                         host='localhost')

    # for with statement
    def __enter__(self):
        return self.connection_pool.getconn()  # connection has attribute 'cursor'

    # for with statement
    def __exit__(self, exc_type, exc_val, exc_tb):
        # We really should be returning the connections, but how?
        pass
