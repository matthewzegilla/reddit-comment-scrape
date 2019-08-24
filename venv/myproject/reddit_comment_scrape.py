# Designed by Matt 8-24-19 :)
# Searches all comments in a given subreddit for a given list
# and outputs username and what keyword they wrote into a database.

import praw
from praw.models import MoreComments
from RedditBotSQLLite import add_comment

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("Politics").hot(limit=100)

my_search_keywords = ['Bernie', 'Warren', 'Biden', 'Harris', 'Yang', 'Buttigieg', "O'Rourke", 'Booker', 'Gabbard', 'Castro']


def search_comments(search_words):
    for post in subreddit:
        for comment in post.comments:
            if isinstance(comment, MoreComments):
                continue
            for keyword in search_words:
                if keyword in comment.body:
                    comment_author = comment.author
                    add_comment(comment_author.name, keyword)

search_comments(my_search_keywords)