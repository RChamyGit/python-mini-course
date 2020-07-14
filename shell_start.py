import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")

        dst = src + ".bak"

        # shutil.copy(src, dst)

        # #pra copiar metadados precisa de copystat

        # shutil.copystat(src, dst)

        # #renomear o arquivo original

        # os.rename("textfile.txt", "newfile.txt")

        # #zipar

        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)
        # #zipa o arquivo todo

        #more fine-grained zip files
        with ZipFile ("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()