class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        sett=set(nums)
        for i in nums:
            curr,sterk=i,0
            while curr in sett:
                curr+=1
                sterk+=1
            res=max(res,sterk)
        return res        

                   
        