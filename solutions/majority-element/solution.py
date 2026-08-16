# LeetCode Problem: 169. Majority Element
# Language: Python3
# Submission ID: 2108017161
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key=0
        max_count=0
        nums.sort()
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for i in seen:
            if max_count<seen[i]:
                max_count=seen[i]
                key=i
        return key
                



        