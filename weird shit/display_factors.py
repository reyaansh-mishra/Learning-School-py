def get_factors(number: int):
    current_factor = 1
    while (current_factor < number/2 + 1):
        if (number % current_factor == 0):
            print(current_factor)
        current_factor += 1

usr_input = int(input("Enter Number: "))
get_factors(usr_input)