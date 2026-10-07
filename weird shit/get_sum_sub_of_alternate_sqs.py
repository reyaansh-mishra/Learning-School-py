meth            = 1
start_num       = 2
counter         = 0
number_of_terms = int(input("Gimme Number of Terms: "))

while counter < number_of_terms:
    print("LOOP", counter)
    number = counter**2

    if (number%2 == 0):
        meth += number
        print("PLUS")
    else:
        meth -= number
        print("MINUS")

    counter+=1
print(meth)