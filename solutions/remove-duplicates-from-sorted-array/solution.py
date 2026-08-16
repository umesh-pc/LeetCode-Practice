# LeetCode Problem: 26. Remove Duplicates from Sorted Array
# Language: Python3
# Submission ID: 2103970009
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=sorted(set(nums))
        for i in range(len(n)):
            nums[i]=n[i]
        return len(n)
        