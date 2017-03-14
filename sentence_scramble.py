'''
Created on Jan 25, 2017

@author: Evan
'''
#from chain import Chain
#from utility import get_tweets
from utility import folderlink
#from markovify import chain
import markovify
#I know a lot of these imports are un-used. Im going to go through and clean these up once this thing is actually up and running in case I need to jimmy around with stuff more
#and not need to import/un-import a million things



#this is currently an attempt to actually have markov assemble gibberish
        
def write_file(tweets):
    with open((folderlink + "markov_sentences.txt"), "w") as text_file:
    
        #this is the destination of the corpus as declared in the chain function of markovify
    
        text_file.write (tweets[1:-1])
        
        #writes tweets without the "[]" at the beginning and the end. Perhaps the "None" error is happening here and below it?
        #ok, definitetly not happening in the above code. That leaves the below
        
        with file ((folderlink + "markov_sentences.txt"), 'r') as f:
            text = f.read()
        
        #put your own filepath here ^
        
        text_model = markovify.Text(text)
         
        
        for i in range(5):
            print(text_model.make_short_sentence(140, tries=100))
            #so either the hiccup is happening here or 4 lines above this comment. Or maybe something is wrong with the path itself. Im not really sure why its returning "None"
        
            #ok, further poking and prodding reveals that the code is in fact compiling and attempting to read a file. However it is defaulting to none as seen in the chain code.
            #however it is unable to make anything of what its reading and returning nothing as a result. Maybe its not liking how the text is formatted? Im betting thats going to be the problem
            
        
        
        text_file.close() 
        
    

#make a function that wipes the file when its done with it you fuck