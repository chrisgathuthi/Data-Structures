
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    l, r = 0, 1 #l=buy, r=right
    maxprofit = 0

    while r < len(prices):

        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxprofit = max(profit, maxprofit)
        else:
            l = r 
        r += 1
    return maxprofit

window = [2,5,7,20, 30]
results = maxProfit(window)
print(results)

"""
time complexity 0(n)
space complexity 0(1)

The sliding window, the first element is always the buy hence we iniitilise the right to index 1
when the right is lower than the left it means there's a loss and at all times the selling price should
not be less than the buying price therefore we move the left to right.
"""