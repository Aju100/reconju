'''
import urllib.request
import io
# GET ROBOTS.TXT FILE
def getRobot(url):
    if url.endswitch('/'):
        path = url
    else:
        path = url +'/'
    
    request = urllib.request.urlopen(path+"robots.txt",data=None)
    data = io.TextIOWrapper(request,encoding='utf-8')

    return data.read

print(getRobot('https://www.facebook.com'))
'''

import requests
url = input("Enter URL : ")

robots = requests.get(url+"/robots.txt")
print(robots.text)
