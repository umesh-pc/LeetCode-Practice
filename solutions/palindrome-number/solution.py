# LeetCode Problem: 9. Palindrome Number
# Language: Python3
# Submission ID: 2100948477
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=int(str(abs(x))[::-1])
        if x==rev:
            return True
        else:
            return False
        