# Removing a Range of Elements From a List

l = [1,2,3,4,5,6,7,8,9,10]

start   = int(input("Start: "))
end     = int(input("End: "))

if (start >= end):
        for i in range(start, end+1, 1):
                l.remove(i)
else:
        for i in range(start, end, -1):
                l.remove(i)

print(l)