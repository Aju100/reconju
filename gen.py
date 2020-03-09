import os

# CREATE A NEW DIRECTORY
def create(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

# WRITE DATA TO A FILE
def write(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

    