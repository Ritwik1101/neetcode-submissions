class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        seet=set(nums)
        hashmp={val:nums.count(val) for val in seet  }
        sortedd = sorted(hashmp.items(), key=lambda x: x[1], reverse=True)
        res=[]
        for i in sortedd:
            res.append(i)
            if len(res)==k:
                return res    
        