def robbers(nums):
    
    if len(nums) < 1:
        return 0

    if len(nums) == 1:
        return nums[0]
    
    loot = [0] * len(nums)
    loot[0] = nums[0]
    loot[1] = max(nums[0], nums[1])

    length = len(nums)

    for elem in range(2, len(nums)):
        loot[elem] = max(nums[elem] + loot[elem - 2], loot[elem - 1])
    return loot[length - 1]


nums = [1,2,3,1]
res = robbers(nums)
print(res)
