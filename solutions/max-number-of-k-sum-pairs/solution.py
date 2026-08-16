# LeetCode Problem: 1679. Max Number of K-Sum Pairs
# Language: Python3
# Submission ID: 2107895774
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=len(nums)-1
        i=0
        c=0
        while i<l:
            if k==nums[i]+nums[l]:
                c+=1
                i+=1
                l-=1
            elif k>nums[i]+nums[l]:
                i+=1
            else:
                l-=1
        return c
