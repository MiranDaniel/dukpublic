import os
import praw
import sql
from datetime import datetime
import pathlib
from logger import log
import itertools

from utils import(
SUBREDDIT,
REMOVED_FLAIR_CONTAINS
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

def main():
    for i in itertools.count():
        for submission in reddit.subreddit(SUBREDDIT).new(limit=None):
            if str(REMOVED_FLAIR_CONTAINS) in str(submission.link_flair_text):
                try:
                    if sql.check_existence(str(submission.author.name)) == False:
                        sql.insert(str(submission.author.name), 1)
                    else:
                        sql.change_val(str(submission.author.name))
                    submission.mod.remove()
                except Exception as e:
                    log.critical(e)
                    log.critical("Missing permission to remove posts (Posts)")
                    quit()
                else:
                    log.info("Removed submission "+submission.id)


if __name__ == "__main__":
    main()