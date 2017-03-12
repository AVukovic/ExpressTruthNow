'''
Created on Jan 25, 2017

@author: Evan
'''
from chain import Chain
from utility import get_tweets
from main import tweet
from main import tweets
from markovify import chain
import markovify
#I know a lot of these imports are un-used. Im going to go through and clean these up once this thing is actually up and running in case I need to jimmy around with stuff more
#and not need to import/un-import a million things



#this is currently an attempt to actually have markov assemble gibberish
        
def write_file():
    with open("C:/Users/Evan/Desktop/Markov_Bot/markovwrite/markov_sentences.txt", "w") as text_file:
    
        #this is the destination of the corpus as declared in the chain function of markovify
    
        text_file.write (str(tweets)[1:-1])
        
      
        
        with file ('C:/Users/Evan/Desktop/Markov_Bot/markovwrite/markov_sentences.txt', 'r') as f:
            text = f.read()
        
        #put your own filepath here ^
        
        text_model = markovify.Text(text)
         
        
        for i in range(5):
            print(text_model.make_short_sentence(140, tries=100))
            
            #got the "None" error fixed! see utility file for where it was fixed
        text_file.close() 
        
    
write_file()

#make a function that wipes the file when its done with it you fuck