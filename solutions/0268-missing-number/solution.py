class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        m=len(nums)
        rs=sum(range(m+1))
        d=rs-s
        return d
