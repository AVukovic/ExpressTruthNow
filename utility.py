
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
            "SECRET": returns secret API key
            "ACCESS": returns access key
            "SECACCESS": returns secret access key
            "ALL": returns username, password, API, and secret API
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
    
    elif (info == "SECRET"):
        try:
            start = infofile.index("(secret)") + len ("(secret)")
            end = infofile.index("(secretend)")
            return infofile[start:end]
        except ValueError:
                print "Error: Invalid File Format"
    
    elif (info == "ACCESS"):
        try:
            start = infofile.index("(access)") + len ("(access)")
            end = infofile.index("(accessend)")
            return infofile[start:end]
        except ValueError:
                print "Error: Invalid File Format"
        
    elif (info == "SECACCESS"):
        try:
            start = infofile.index("(accesssecret)") + len ("(accesssecret)")
            end = infofile.index("(accesssecretend)")
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
            
            secretstart = infofile.index("(secret)") + len ("(secret)")
            secretend = infofile.index("(secretend)")
            print ("SECRET: ") + infofile[secretstart:secretend]
            
            accessstart = infofile.index("(access)") + len ("(access)")
            accessend = infofile.index("(accessend)")
            print ("ACCESS: ") + infofile[accessstart:accessend]
            
            accesssecretstart = infofile.index("(accesssecret)") + len (
            "(accesssecret)")
            accesssecretend = infofile.index("(accesssecretend)")
            print ("ACCESS SECRET: ") + infofile[accesssecretstart:
                accesssecretend]
        except ValueError:
            print "Error: Invalid File Format"
            
    else: print ("Error: Invalid File Format")

            
        
        
    
            