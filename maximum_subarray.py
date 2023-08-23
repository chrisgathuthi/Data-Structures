# kadane's problem

def maxSubArray(array):

    maxsub = array[0]
    current_sum = 0

    for i in array:

        if current_sum < 0:
            current_sum = 0

        current_sum += i
        maxsub = max(current_sum, maxsub)
    return maxsub 


test = [-2, 2, 5, -11, 6]
result = maxSubArray(test)
print(result)

"""
notes
"""

# If the current sum currentSum becomes negative, 
# it indicates that including the current element in 
# the subarray would reduce the overall sum. 
# In such cases, we reset currentSum to 0.
# This effectively discards the current subarray and
# allows us to start a fresh subarray from the next element.