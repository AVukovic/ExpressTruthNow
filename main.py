
"""
main.py is the main script for running and interacting with the ETS twitter.
"""

import tweepy
import utility

"Currently a test that works successfully. Will update file."

path = raw_input("Enter url of info file: ")

key = utility.returninfo(path, "API")
secret = utility.returninfo(path, "SECRET")
access = utility.returninfo(path, "ACCESS")
secaccess=utility.returninfo(path, "SECACCESS")                          

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, secaccess)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
    print " NEXT \n"