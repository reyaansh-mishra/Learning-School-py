''' Amstrong Number:
        Sum of the cube of the digits = number
'''

def check_if_armstrong(num: int) -> bool:
    sum = 0
    num_2_use = num

    while (num_2_use != 0):
        current_number = num_2_use%10
        sum += (current_number**3)
        num_2_use //= 10

    if (sum == num):
        return True
    return False

number = int(input("Number: "))
print("\n", check_if_armstrong(number), sep="")