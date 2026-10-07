itr  = 0

while (itr < 10):
    itr+=1
    if (itr > 5):
        continue
    print("Hi", itr)

print("\n", itr)

for number in range(1,20):
  if number==7:
    print("HAHAHAHA")
    break
  else:
    print(number)
print("did we break?")