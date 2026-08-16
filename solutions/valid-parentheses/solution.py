# LeetCode Problem: 20. Valid Parentheses
# Language: Python3
# Submission ID: 2098552296
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        stack=[]
        dic={'(':')','{':'}','[':']'}
        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if stack==[]:
                    return False
                a=stack.pop()
                if i !=dic[a]:
                    return False
        return stack==[]
        