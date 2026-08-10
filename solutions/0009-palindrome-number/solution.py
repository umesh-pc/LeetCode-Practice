class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=int(str(abs(x))[::-1])
        if x==rev:
            return True
        else:
            return False
        
