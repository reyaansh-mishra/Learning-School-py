def reverse_num(num: int) -> int:
    reverse = 0
    tmp_num = num

    while (tmp_num != 0):
        fst_digit   = tmp_num%10
        reverse     = (reverse * 10) + fst_digit
        tmp_num     //= 10

    return reverse


print(reverse_num(int(input("Enter Num: "))))