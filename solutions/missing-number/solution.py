# LeetCode Problem: 268. Missing Number
# Language: Python3
# Submission ID: 2093570479
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(0,len(nums)+1))-sum(nums)