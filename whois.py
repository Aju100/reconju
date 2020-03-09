import os

def getWhois(url):

    command ="whois "+url
    process = os.popen(command)
    results = str(process.read())

    return results

print (getWhois('facebook.com'))