import urllib.request
import io


def getRobot(url):
    if url.endswitch('/'):
        path = url
    else:
        path = url +'/'
    
    request = urllib.request.urlopen(path+"robots.txt",data=None)
    data - io.TextIOWrapper(request,encoding='utf-8')

    return data.read

print(getRobot('https://www.facebook.com'))

