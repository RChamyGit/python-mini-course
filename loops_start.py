def main():

    x = 0

    #definir while

    while (x<5):
        print(x)
        x = x+1

    #define a for loop
    
    x = 0
    print("resetou")

    # for x in range(5, 10):
    #     print(x)

    for x in range (5,10): #cuidado c a indentacao, ela q define quem ta dentro de quem
    # if (x==7): break
        if ( x % 2 == 0): continue #continue termina a iteracao e inicia a proxima
        #break interrompe o loop
        print(x)

    #use a for loop over a collection
    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days): #enumerate tmbem retorna index 
        print(i, d)

if __name__ == "__main__":
    main()