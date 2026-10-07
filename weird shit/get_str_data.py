def info(s: str):
    alp,space,char,digits=0,0,0,0

    for i in s:
        char += 1
        if i.isalpha():
            alp += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digits += 1

    return alp,space,char,digits

def main():
    usr_input = input("String: ")

    alp,space,char,digits = info(usr_input)

    print("\n\r", alp,space,char,digits, sep="\n\r")

if __name__ == "__main__":
    main()