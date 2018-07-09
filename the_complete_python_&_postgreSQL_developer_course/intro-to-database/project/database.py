import psycopg2


def connect():
    return psycopg2.connect(user='postgres', password='root1224', database='learning',
                            host='localhost')
