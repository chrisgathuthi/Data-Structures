
def two_sum_sorted(nums, target):
    """
    Assumes that the array is sorted
    """
    left, right = 0, len(nums) - 1

    while left < right:

        current_sum = nums[left] + nums[right]

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]
    return []

arr = [2,7,11,15]
tar = 9

res = two_sum_sorted(arr, tar)
print(res)