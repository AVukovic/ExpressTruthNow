
"""
utility.py is a collection of methods that assist in reading, writing, and 
formatting text strings, such as tweets.


"""

def returninfo(address, info="ALL"):
    """ 
    Reads the info file provided, and returns relevant information based on 
    user request.
    
    Args:
        path: file destination (str)
        
        info: specific piece of information to return. Potential information to
        return includes:
            "USER": returns username
            "PASS": returns password
            "API": returns API key    
            "ALL": returns username, password, and API
    """
    infofile = open(address, 'r').read() #opens file, returns as string
    
    if (info == "USER"): #elseif chain based on input
        try:
            start = infofile.index("(user)") + len("(user)")
            end = infofile.index("(userend)")
            return infofile[start:end]
        except ValueError:
            print "Error: Invalid File Format"
    
    elif (info == "PASS"):
        try:
            start = infofile.index("(pass)") + len("(pass)")
            end = infofile.index("(passend)")
            return infofile[start:end]
        except ValueError:
            print "Error: Invalid File Format"
            
    elif (info == "API"):
        try:
            start = infofile.index("(api)") + len("(api)")
            end = infofile.index("(apiend)")
            return infofile[start:end]
        except ValueError:
            print "Error: Invalid File Format"
            
    elif (info == "ALL"):
        try:
            userstart = infofile.index("(user)") + len("(user)")
            userend = infofile.index("(userend)")
            print ("USERNAME: " + infofile[userstart:userend])
            
            passstart = infofile.index("(pass)") + len("(pass)")
            passend = infofile.index("(passend)")
            print ("PASSWORD: " + infofile[passstart:passend])
            
            apistart = infofile.index("(api)") + len("(api)")
            apiend = infofile.index("(apiend)")
            print ("API: " + infofile[apistart:apiend])
        except ValueError:
            print "Error: Invalid File Format"
            
    else: print ("Error: Invalid File Format")

            
        
        
    
            