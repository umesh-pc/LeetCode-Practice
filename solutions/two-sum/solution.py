# LeetCode Problem: 1. Two Sum
# Language: Python3
# Submission ID: 2109053586
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem=0
        for i,num in enumerate(nums):
            rem=target-num
            if rem in nums:
               j= nums.index(rem)
               if i!=j:
                    return [i,j]
        