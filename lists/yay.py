#Given a Python list, remove all occurrence of 20 from the list

def removeList(lst: list[int], val_to_kill: int):
    final: list[int] = []
    for i in lst:
        if (i != val_to_kill):
            final.append(i)
    return final

list1 = [5, 20, 15, 20, 25, 50, 20]
print(removeList(list1, 20))