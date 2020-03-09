from domain import *
from gen import create, write
from ip import *
from robot import *
from scan import get
from whois import getWhois


DIRECTORY = 'pentesting'

create(DIRECTORY)

def gather(name,url):
    robots_txt = getRobot(url)
    domain_name = get_Domain(url)
    ip_address = getIp(domain_name)
    nmap = get('-F',ip_address)
    whois = getWhois(domain_name)

    create_report(name,url,domain_name,nmap,robots_txt,whois)

def create_report(name,url,domain_name,nmap,robots_txt,whois):
    DIR = DIRECTORY+'/'+name
    create(DIR)

    write(DIR+"/full_url.txt",url)
    write(DIR+"/domain_name.txt",domain_name)
    write(DIR+"/nmap.txt",nmap)
    write(DIR+"/robots.txt",robots_txt)
    write(DIR+"/whois.txt",whois)

get('google','https://www.google.com')


