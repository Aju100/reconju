import os

def get(options,ip):

    command ="nmap " +options+" "+ip
    process = os.popen(command)

    results = str(process.read())

    return results

print(get('-Pn','103.192.77.232'))