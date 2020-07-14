import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    print("item existsd: " + str(path.exists("textfile.txt")))
    print("item is a file " + str(path.isfile("textfile.txt")))
    print("item is a directory " + str(path.isdir("textfile.txt")))

    print("item path: " + str(path.realpath("textfile.txt")))
    print("item path and name: " + str(path.isdir("textfile.txt")))

    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp (path.getmtime("textfile.txt"))
    print("ja se passou" +str(td) + "desde que o arquivo foi modificado")
    print("ou," + str(td.total_seconds()) + "segundos")

if __name__ == "__main__":
    main()