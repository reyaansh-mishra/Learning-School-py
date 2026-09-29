# rows = 5
# for i in range(rows+1):
#     for a in range(5-i):
#         print(a, end=" ")
#     print()

# rows = 5
# for i in range(rows, 0, -1):
#     for a in range(0, i+1):
#         print(a, end=" ")
#     print()

# Print nos Triag from 1 -> 10

start_num   = 1
end_num     = 10

print_no_of_chars   = 1
last_num = 1

print_nos = 1

for i in range(start_num, end_num+1):
    current_num = i + (last_num-1)
    j = 0

    for j in range(print_nos):
        if (j+last_num > end_num): break
        print(j+last_num, end = " ")

    if (j+last_num > end_num): break

    print_nos+=1
    last_num=current_num
    print()

