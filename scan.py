import os

def get(options,ip):

    command ="nmap " +options+" "+ip
    process = os.popen(command)

    results = str(process.read())

    return results

print(get('-o','54.186.250.79'))