import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="chicagocrime",
        user="postgres",
        password="040626xw",
        host="localhost",
        port="5432"
    )