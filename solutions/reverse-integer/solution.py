# LeetCode Problem: 7. Reverse Integer
# Language: Python3
# Submission ID: 2100942264
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        limt=1<<31
        sing = -1 if x < 0 else 1
        r= sing*int(str(abs(x))[::-1])
        if r<-limt or r>(limt-1):
            return 0
        return r