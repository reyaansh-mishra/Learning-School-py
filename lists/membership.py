# give me second highest

def get_second_highest(nums: list[int]):
    max_1 = max(nums)
    max_2: int = nums[0]

    for i in range(1, len(nums)):
        if (nums[i] != max_1) and (nums[i] > max_2):
            max_2 = nums[i]
    return max_2

print(get_second_highest([0,1,2,3,4,5,6,7]))
