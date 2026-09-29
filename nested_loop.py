#  FUCK YOU NESTED LOOPS

for i in range(10):
    for a in range(10):
        if (i == a):
            print("HAHA")
            continue
        print("i = ", i, " a = ", a, sep="")

# Print Pyramid

def print_pyramid_inverse():
    for i in range(5,0, -1):
        for a in range(1, i+1): # type: ignore
            print(a, end=" ")
        print()

def print_pyramid():
    for i in range(1,6):
        for a in range(1, i+1): # type: ignore
            print(a, end=" ")
        print()

def one_pyra_inverse():
    for i in range(1,6):
        for a in range(6-i, 0, -1):
            print(i, end=" ")
        print()

print("\n\n\n\n")
print_pyramid_inverse()
print_pyramid()
print()
one_pyra_inverse()