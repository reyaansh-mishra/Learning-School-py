# Lists Suck

list1 = [10,20,30,40,50,60]
print(list1[3:6])
print(list1[-1:3:-1])

newList = list1[3:]
print(newList)
print(type([]))

def count_num_occurrence(list_the_list: list[int], val: int) -> int:
    ctr: int = 0
    for i in range(len(list_the_list)):
        if (list_the_list[i] == val):
            ctr+=1
    return ctr

print(count_num_occurrence([123, 2323, 63, 888, 63], 63))

def if_even_add_to_list():
    list: list[int] = []

    while True:
        num = int(input("0 to kill. Try Me: "))

        if (num == 0):
            print(list)
            break
        if (num % 2 == 0):
            list.append(num)

if_even_add_to_list()

a = [2,5,6,7,3]
a[1:] = 54
print(a)