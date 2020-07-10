


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method 2"+ someString)

class anotherClass():
    def method1(self):
        print("myClass method2")

def main():
    c = myClass() #similar ao java..
    c.method1()
    c.method2("string aqui")

    c2 = anotherClass()

if __name__ == "__main__":
    main()