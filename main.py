
"""
main.py is the main script for running and interacting with the ETS twitter.
"""

import utility

tweets = utility.get_tweets(utility.login())
for tweet in tweets:
    print (tweet.encode("utf-8"))
    #added utf-8 enconding 
    print "\n"
