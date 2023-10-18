def climbStairs(self, n: int) -> int:

    # one staircase
    if n <= 1: return 1
    steps = [0] * (n + 1)
    steps[1] = 1
    steps[2] = 2
    for i in range(3, len(steps)):
        steps[i] = steps[i - 1] + steps[i - 2]
    return steps[n]

"""
The tabulation approach of creating holding table.
"""

def climbStairs2(self, n: int) -> int:

    if n <= 1: return 1

    previous, current = 1, 1

    for i in range(2, n + 1):
        temp = current
        current = previous + current
        previous = temp
    return current
"""
The value of current is previous plus current
The previous is assigned temp because temp was holding
the previous value of current before it is updated hence it is 
assigned to previous
"""
