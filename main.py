
"""
main.py is the main script for running and interacting with the ETS twitter.
"""

import utility
import sentence_scramble

tweets = utility.get_tweets(utility.login(), num=100)
new_tweets = str(tweets)
print "NEW TWEETS\n\n\n"
print new_tweets
print "TWEETS"
for tweet in tweets:
    #print (tweet.encode("utf-8"))
    #added utf-8 enconding 
    print "\n"
print "MARKOV"
sentence_scramble.write_file(new_tweets)
