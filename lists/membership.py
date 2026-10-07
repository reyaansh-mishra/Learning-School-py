# give me second highest

def get_second_highest(nums: list[int]):
    max = nums[0]
    secnd_max: int = 0
    if (max > nums[1]):
        secnd_max = nums[1]
    else:
        secnd_max = nums[0]
        max = nums[1]
    for i in range(max+1): # Start at 2nd pos
        if 
print([2,4,6] > [2,5,3])