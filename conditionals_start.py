# exemplo condicoes

def main():
    x, y = 100, 90

    # conditional flow uses if, elif, else
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"
    print (st)

    st="x is less than y" if (x<y) else "x is greater than or the same as"

if __name__ == "__main__":
    main()
#python nao tem switch case
