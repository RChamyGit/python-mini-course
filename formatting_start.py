from datetime import datetime

def main():
    now = datetime.now()
    
    print(now.strftime("a DATA ATUAL EH: %Y"))
    print(now.strftime("%a, %d %B, %y")) #dia da semana, dia do mes, nome mes, ano
    print(now.strftime("Locale Date and Time: %c"))

    print(now.strftime("locale date: %x"))
    print(now.strftime("locale time: %X"))

    print(now.strftime("Current time: %I:%M:%S %p")) #AM PM
    print(now.strftime("24 hour time: %H %M"))

if __name__ == "__main__":
    main();
