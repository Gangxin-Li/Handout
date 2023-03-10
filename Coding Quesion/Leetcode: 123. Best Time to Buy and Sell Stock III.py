# Time: Sat, Feb, 25, 2023 2:25:23 PM GMT
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 105
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_hold, first_sell = -float('inf'),0
        second_hold, second_sell = -float('inf'),0

        for price in prices:
            # Finally we sell our second stock to get the money
            second_sell = max(second_sell, second_hold + price)
            # and then we need to buy the second one, here we use the current money, that is first_sell - current
            second_hold = max(second_hold, first_sell - price)
            # Then we can sell it as a profile, here we can use current price + (-price) to get the profile.
            first_sell = max(first_sell, first_hold + price)
            # First, if you want to buy a stock, we should pay for the price, so it is - number
            first_hold = max(first_hold,0 - price)
        return second_sell