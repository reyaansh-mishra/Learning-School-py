def check_prime(number: int) -> bool:
    for i in range(2, number):
        if (number%i == 0): return False
    return True

usr_input = int(input("Enter Number: "))
print(check_prime(usr_input))