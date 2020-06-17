import psycopg2
from datetime import datetime
from logger import log

from login import(
sql_user,
sql_password,
sql_host,
sql_database
)


try:
    connection = psycopg2.connect(user = sql_user,
                                  password = sql_password,
                                  host = sql_host,
                                  port = "5432",
                                  database = sql_database)
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    log.info("You are connected to - "+str(record))

except (Exception, psycopg2.Error) as error:
    log.critical("Error while connecting to PostgreSQL "+str(error))
    exit()


def check_existence(val0):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from public.ban"
        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        for row in db:
            if row[0] == val0:
                return True
        else:
            return False
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)



def return_values(val0):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = f"SELECT * FROM PUBLIC.BAN WHERE u LIKE \'{val0}\'"
        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        for row in db:
            if row[0] == val0:
                print(row[0])
                print(row[1])

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)


def insert(val0,val1):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO ban (u, rems) VALUES (%s,%s)"""
        record_to_insert = (val0,val1)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)


def change_val(value, hm=1):
    try:
        cursor = connection.cursor()
        postgres_insert_query = str("UPDATE public.ban SET rem_posts=rem_posts+{} WHERE u='{}'").format(hm,value)
        cursor.execute(postgres_insert_query)

        connection.commit()
        count = cursor.rowcount

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)



def test():
    try:
        from ban import banner
        cursor = connection.cursor()
        postgreSQL_select_Query = f"SELECT * FROM PUBLIC.BAN WHERE rem_posts > 4"
        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        for row in db:
            ban.ban(row[0])
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)



