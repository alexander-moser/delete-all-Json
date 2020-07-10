import os
import re

def openAndDeleteAllJson(dir):
    os.chdir(str(dir))

    for filename in os.listdir():
        if filename.endswith('.json'):
            os.remove(filename)
            print("Removed " + filename)
            
    os.chdir('..')

def main():
    print("Start")

    for filename in os.listdir():
        if filename != "removeAllJson.py":
            openAndDeleteAllJson(filename)

    print("Finished!")

if __name__ == '__main__':
    main()