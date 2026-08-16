# LeetCode Problem: 70. Climbing Stairs
# Language: Python3
# Submission ID: 2106803318
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
        return second 