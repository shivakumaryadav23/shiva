def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

nums = [11, 12, 14, 13, 14, 13, 15, 14
print(test(nums))