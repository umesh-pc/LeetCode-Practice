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
        
