import os

# GET IP ADDRESS
def getIP(url):

    command = "host "+url
    process = os.popen(command)
    results = str(process.read())

    marker = results.find('has address')+12
    
    return results[marker:].splitlines()[0]

print(getIP('facebook.com')) 