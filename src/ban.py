import praw
from logger import log

from utils import(
POINT_LIMIT,
BAN_LENGTH,
BAN_REASON,
BAN_MESSAGE,
BAN_NOTE,
SUBREDDIT

)



from login import(
reddit_client_id,
reddit_client_secret,
reddit_user_agent,
reddit_username,
reddit_password
)


# REDDIT LOGGING
try:
    reddit = praw.Reddit(client_id=reddit_client_id,
                        client_secret=reddit_client_secret,
                        user_agent=reddit_user_agent,
                        username=reddit_username,
                        password=reddit_password)

    if reddit.read_only == False:
        log.info("Logged in as u/"+reddit.user.me().name)
    else:
        log.critical('Reddit is read only')
        log.critical("Login credentials are missing.")
        quit()

except Exception as e:
    log.critical(e)
    log.critical("Login credentials are not correct.")
    quit()



def banner(arg):
    try:
        reddit.subreddit(SUBREDDIT).banned.add(arg, duration=BAN_LENGTH, ban_reason=BAN_REASON, ban_message=BAN_MESSAGE, note='')
    except Exception as e:
        log.critical(e)
        log.critical("Missing permission to ban (Access)")
    else:
        log.info(f"Banned {arg} for {BAN_LENGTH}")
        reset(val)


def reset(val):
    try:
        cursor = connection.cursor()
        postgres_insert_query = str(f"DELETE FROM ban WHERE u='{val}'")
        cursor.execute(postgres_insert_query)
        connection.commit()


    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)