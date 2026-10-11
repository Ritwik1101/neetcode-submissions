class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        hset=set(nums)
        small=min(hset)
        count=1
        for i in nums:
            if small+1 in hset:
                small+=1
                count+=1
            else :
                break
                
        return count            
        