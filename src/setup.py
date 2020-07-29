import psycopg2
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

def setup():
    def create_table():
        try:
            cursor = connection.cursor()
            postgreSQL_select_Query = """
            CREATE TABLE ban(
                u VARCHAR(32),
                rems INT);
            """

            cursor.execute(postgreSQL_select_Query)
            connection.commit()
            check_tables()
        except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert record into mobile table", error)

    def check_tables():
        try:
            cursor = connection.cursor()
            postgreSQL_select_Query = """
            SELECT
                table_schema || '.' || table_name
            FROM
                information_schema.tables
            WHERE
                table_type = 'BASE TABLE'
            AND
                table_schema NOT IN ('pg_catalog', 'information_schema');
            """
            cursor.execute(postgreSQL_select_Query)
            db = cursor.fetchall()
            for row in db:
                if row[0] == "public.ban":
                    log.info("setup finished")
                    exit()
        except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert record into mobile table", error)

    if check_tables() == "OK":
        pass
    else:
        create_table()


setup()