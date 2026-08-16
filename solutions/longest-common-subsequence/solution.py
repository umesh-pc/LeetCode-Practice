# LeetCode Problem: 1143. Longest Common Subsequence
# Language: Python3
# Submission ID: 2060341589
# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Ensure text2 is the shorter string to minimize space
        if n > m:
            text1, text2 = text2, text1
            m, n = n, m
        
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev, curr = curr, prev
        
        return prev[n]