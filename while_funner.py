num   = 10
while (num > 0):
    print(num)
    num -= 1

print()
print()
print()

number      = int(input("Gimme number: "))
count_max   = 10
count       = 0
count_odd   = 0
number      += 1
while count_odd < count_max:
    if count % 2 == 0:
        print(number + count)
        count_odd += 1
    count+=1