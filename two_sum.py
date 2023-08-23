
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    table = {}
    for index, elem in enumerate(nums):
        compliment = target - elem
        if compliment in table:
            return [table[compliment], index]
        table[elem] = index
    print(table)
    return []

nums = [2, 7, 11, 15]
target = 9
v = twoSum(nums= nums, target= target)
print(v)
