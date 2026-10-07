sum = 0

while (True):
    usr_input = int(input("Enter Number: "))

    if (usr_input == 0):
        print("Sum is: ", sum)
        break

    if (usr_input % 2 == 0):
        sum += usr_input
    