"""bot that takes recommended songs from r/listentothis on reddit,
selects 10 highest-ranked on youtube and posts a comment on r/listentothis."""

import praw
import bs4



"""
reddit block:
- read r/listentothis posts from a set time interval
- get (20) top comments with youtube links
- post new comment featuring generated list
"""


"""
youtube block:
- enters URL of video
- scrapes views and likes\dislikes data
"""


"""
logic block:
- receives views and likes/dislikes data
- aggregates data 
- computes 10 "best" videos
"""