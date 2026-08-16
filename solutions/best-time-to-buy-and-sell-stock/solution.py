# LeetCode Problem: 121. Best Time to Buy and Sell Stock
# Language: Python3
# Submission ID: 2107153658
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        current_min=float('inf')
        for i in prices:
            if i<current_min:
                current_min=i
            if i>current_min and i-current_min>best:
                best=i-current_min

        
        return best
        