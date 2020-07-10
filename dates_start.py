from datetime import date
from datetime import time
from datetime import datetime

def main():
    #DATE OBJECTS
    #imprimir a data de hoje
    # today = date.today()
    # print("hoje é: ", today)
    # print("descricao do date: ", today.day, today.month, today.year)

    # print("dia da semana eh o #:", today.weekday())
    # days = ["mon","tue","wed","thu","fri","sat","sun"]

    # print("que eh em ingles: ", days[today.weekday()])

    today = datetime.now()
    print("a data e hora atual eh: ", today)

    t = datetime.time(datetime.now())
    print(t)

if __name__ == "__main__":
    main() 