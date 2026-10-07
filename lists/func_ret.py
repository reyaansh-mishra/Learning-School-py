def gimme_list_till_n(n: int) -> list[int]:
    list: list[int] = []
    for i in range (n+1):
        list.append(i)
    return list

print(gimme_list_till_n(17)) 