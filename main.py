
"""
main.py is the main script for running and interacting with the ETS twitter.
"""

import utility
import codecs

tweets = utility.get_tweets(utility.login())
for tweet in tweets:
    
    f = codecs.open('tweet', encoding='utf-8', mode='w+')
    #tweet.encode('ascii')
    f.write(u'tweet''.')
    #print (tweet)
    #.encode("utf-8"))
    #^ in regards to this above line of code. It is designed to after tweet in the parenthesis on line 10. I am taking it out for the moment to work with some library errors when trying to print tweets
    #added utf-8 enconding 
    print "\n"
