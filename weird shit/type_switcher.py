def change_letter(l: str):
    tmp_l = ""
    if l.islower():
        tmp_l += l.upper()
    else: # Upper
       tmp_l += l.lower()

    return tmp_l

def change_case_say_pls(s: str):
    temp_str = ""

    for i in s:
        temp_str += change_letter(i)
    return temp_str

def main():
    usr_input= input("String: ")
    print("\n\r", change_case_say_pls(usr_input))

if __name__ == "__main__":
    main()