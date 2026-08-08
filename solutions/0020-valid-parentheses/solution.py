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
        
