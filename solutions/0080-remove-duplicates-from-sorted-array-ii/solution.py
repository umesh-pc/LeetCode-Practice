class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f=0
        for l in range(len(nums)):
            if f<2 or nums[l]!=nums[f-2]:
                nums[f]=nums[l]
                f+=1
        return f
                

          
        
