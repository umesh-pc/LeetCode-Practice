# LeetCode Problem: 66. Plus One
# Language: Python3
# Submission ID: 2100959478
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       s =int("".join(map(str, digits)))
       s+=1
       return [int(x) for x in str(s)]