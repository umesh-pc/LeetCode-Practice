class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n and (n & n-1)==0:
            return True
        return False
        
