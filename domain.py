from tld import get_tld

def get_Domain(url):

    name = get_tld(url)
    return name

print(get_Domain('https://www.facebook.com'))