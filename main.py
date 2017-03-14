
"""
main.py is the main script for running and interacting with the ETS twitter.
"""

import utility

tweets = utility.get_tweets(utility.login(), num=100)
print "NEW TWEETS\n\n\n"
print "MARKOV"
utility.write_file(tweets)
