def calc_and_print_fb(limit: int):
    x,y     = 0,1
    z       = x+y
    sum     = x+y

    while (z <= limit):
        print(x,y,z)
        x,y = y,z
        z   = x+y

        sum += y+z
    return sum


print("\n", calc_and_print_fb(54))