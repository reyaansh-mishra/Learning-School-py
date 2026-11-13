# Removing a Range of Elements From a List

l: list[int] = [1,2,3,4,5,6,7,8,9,10]

start:  int = int(input("Start: "))
end:    int = int(input("End: "))

for i in range(start, end+1, 1):
        l.remove(i)

print(l)