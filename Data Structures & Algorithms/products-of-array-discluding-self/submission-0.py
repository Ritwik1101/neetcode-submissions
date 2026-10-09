class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        for  i in range(len(nums)):
            pr=1
            for j in range(len(nums)):
                if i==j:
                    continue
                pr*=nums[j] 
            res[i]=pr
        return res          
        