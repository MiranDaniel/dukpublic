import discord
from discord.ext import commands
from datetime import datetime
import logging
import psycopg2
from logger import log


from utils import(
BOT_PREFIX,
BOT_VERSION
)

from login import(
sql_user,
sql_password,
sql_host,
sql_database,
discord_token
)


bot = commands.Bot(command_prefix=BOT_PREFIX)

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


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=str(BOT_VERSION)))
    log.info('We have logged in as {0.user}'.format(bot))

@bot.command(aliases=["fa"])
async def fetchall(ctx, arg=10):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = """
        select * from public.ban
        order by rems DESC
        limit {}
        """.format(arg)

        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        message = []
        for row in db:
            if len(str(message).replace("[","").replace("]","").replace(",","\n")) > 1900:
                await ctx.channel.send("` "+str(message).replace("[","").replace("]","").replace(",","\n").replace("'","")+"`")
                message.clear()
            message.append(f"  {row[1]}  | {row[0]}")
        await ctx.channel.send("` rems | name\n"+str(message).replace("["," ").replace("]","").replace(",","\n").replace("'","")+"`")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            log.error(error)
            await ctx.channel.send(error)


@bot.command(aliases=["f"])
async def fetch(ctx, arg):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = f"""
        SELECT * FROM PUBLIC.BAN
        WHERE u LIKE \'{arg}\'
        """

        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        if str(db) == "[]":
            await ctx.channel.send(f"{arg} not found.")
        for row in db:
            print(row)
            await ctx.channel.send(f"` rems | name\n  {row[1]}    | {row[0]}`")
    except (Exception, psycopg2.Error) as error:
        if(connection):
            log.error(error)
            await ctx.channel.send(error)


@bot.command(aliases=["set"])
async def setter(ctx, arg, whattodo):
    try:
        cursor = connection.cursor()
        postgres_insert_query = str("""
        UPDATE public.ban
        SET rems=rems{}
        WHERE u='{}'
        """).format(whattodo,arg)

        cursor.execute(postgres_insert_query)
        connection.commit()
        await ctx.channel.send(f"Changed values of {arg}")

        cursor = connection.cursor()
        postgreSQL_select_Query = f"""
        SELECT * FROM PUBLIC.BAN
        WHERE u LIKE \'{arg}\'
        """

        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        if str(db) == "[]":
            await ctx.channel.send(f"{arg} not found.")
        for row in db:
            if row[0] == arg:
                await ctx.channel.send(f"{row[0]} | {row[1]} | {row[2]}")

    except (Exception, psycopg2.Error) as error:
        if(connection):
            log.error(error)
            await ctx.channel.send(error)



@bot.command(aliases=["i"])
async def insert(ctx, val0,val1,val2):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """
        INSERT INTO ban 
        (u, rems, bans)
        VALUES (%s,%s,%s)"""
        record_to_insert = (val0,val1,val2)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount

    except (Exception, psycopg2.Error) as error:
        if(connection):
            log.error(error)
            await ctx.channel.send(error)

@bot.command()
async def exe(ctx, *, arg):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """{}""".format(arg)
        cursor.execute(postgres_insert_query)
        connection.commit()
        count = cursor.rowcount
    except (Exception, psycopg2.Error) as error:
        if(connection):
            log.error(error)
            await ctx.channel.send(error)

@bot.command()
async def info(ctx):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = f"SELECT * FROM PUBLIC.BAN"
        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        count = 0
        for row in db:
            count += row[1]

        cursor = connection.cursor()
        postgres_insert_query = """SELECT COUNT(*) FROM BAN"""
        cursor.execute(postgres_insert_query)
        connection.commit()
        db = cursor.fetchall()
        
        for row in db:
            rows = row[0]

        cursor = connection.cursor()
        postgreSQL_select_Query = f"SELECT * FROM PUBLIC.BAN WHERE rems > 4"
        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        savecount = 0
        for row in db:
            savecount += 1


        cursor = connection.cursor()
        postgreSQL_select_Query = f"SELECT pg_size_pretty(pg_database_size('d9iappeap8bpni'));"
        cursor.execute(postgreSQL_select_Query)
        db = cursor.fetchall()
        size = db[0][0]




        await ctx.channel.send(
f"""
Total number of lines = `{int(rows)}`
Total number of points = `{int(count)}`
Current size = `{size}`

Mean point value = `{round(count/rows,2)}`
Mean size per user = `{round(int(size.replace("kB",""))/rows,2)}kB`

Save-able rows = `{savecount} ({round(savecount/rows*100,2)}%)` 
Save-able space = `{round(savecount/int(size.replace("kB","")),2)}kB ({round(savecount/int(size.replace("kB",""))*100,2)}%)`



Connection = `{connection}`

Server status = `{record}`
"""
)




    except (Exception, psycopg2.Error) as error:
        if(connection):
            log.error(error)
            await ctx.channel.send(error)




bot.run(discord_token)
