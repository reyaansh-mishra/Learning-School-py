# GET THE DUPES OUT

def GET_THE_DUPES_OUT(nums: list[int]):
    dupes:      list[int]   = []
    no_dupes:   list[int]   = []

    for num in nums:
        if num not in no_dupes:
            no_dupes.append(num)
        else:
            dupes.append(num)

    return no_dupes, dupes

print(GET_THE_DUPES_OUT([1,2,2,3,3,3,4,4,4,4]))