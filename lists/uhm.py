'''Write a script to accept numbers from the user which are divisible by 7 but
are not multiples of 5 between 2000 and 2500 (both included)
Insert those numbers into a list and display'''

l: list[int] = []

def not_divisible_by_5_we_want(num: int) -> bool:
        if (num >= 2000 and num <= 2500):
                if (num % 5 == 0):
                        return False
        return True


def is_divisible_by_7(num: int) -> bool:
        if (num % 7 == 0):
                return True
        return False

def get_number() -> None:
        num = int(input("Enter Number: "))
        if (is_divisible_by_7(num) and not_divisible_by_5_we_want(num)):
                l.append(num)
                print(l)

while True:
        get_number()
