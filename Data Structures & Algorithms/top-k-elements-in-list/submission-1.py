class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        seet=set(nums)
        hashmp={nums.count(val):val for val in seet  }
        sortedd=dict(sorted(hashmp.items(), reverse=True))
        res=[]
        for i in sortedd:
            res.append(sortedd[i])
            if len(res)==k:
                return res    
        