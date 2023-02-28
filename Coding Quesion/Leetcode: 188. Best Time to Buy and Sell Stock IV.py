# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


# Constraints:

# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Create a init array to maintain the data
        dp = [[-float('inf'),0] for _ in range(k+1)]
        for price in prices:
            for i in range(1,k+1):
                # sell it and we get the profile
                dp[i][1] = max(dp[i][1],dp[i][0] + price )
                # When we hold it, and the profile we get.
                dp[i][0] = max(dp[i][0], dp[i-1][1] - price )
        # print(dp[k])
        return dp[k][1]