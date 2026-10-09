class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        sett=set(nums)
        for i in sett:
            if i-1 not in sett:
                lenn=1
                while i+lenn in sett:
                    lenn+=1
                res=max(res,lenn)    

                
        return res        

                   
        