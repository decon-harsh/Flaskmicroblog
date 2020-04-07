import random
def suggestion(s):
    s=str(s)
    if s[-1].isdigit()==True:
        s=s[:len(s)-1]+str(int(s[-1])+1)
    else:
        s=s[:len(s)]+str(random.randint(0,10))
    return s

def main():
    print(suggestion("harsh1"))


if __name__== "__main__":
    main()