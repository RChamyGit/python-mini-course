def main():
    # f = open("textfile.txt", "w+")

    # f = open("textfile.txt", "a") append add coisas

        # f = open("textfile.txt", "r")

    # for i in range(10):
    #     f.write("this is lineee " + str(i) + "\r\n")

    
    # f.close()
    f = open("textfile.txt", "r") # ler
    

    if f.mode == 'r':
        # contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)

        # print(contents)

main()