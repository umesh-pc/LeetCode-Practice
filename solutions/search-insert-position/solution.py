# LeetCode Problem: 35. Search Insert Position
# Language: Python3
# Submission ID: 2104519370
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i

        return len(nums)
        