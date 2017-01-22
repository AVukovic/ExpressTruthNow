
"""
main.py is the main script for running and interacting with the ETS twitter.
"""

import utility

tweets = utility.get_tweets(utility.login())
for tweet in tweets:
    print tweet
    print "\n"

