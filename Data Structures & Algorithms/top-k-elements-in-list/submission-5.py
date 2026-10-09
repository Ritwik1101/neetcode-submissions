class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        frq = [[] for _ in range(len(nums)+1)]

        for val,cntr in cnt.items():
            frq[cntr].append(val)
        res=[]
        for i in range(len(frq)-1,0,-1)  :
            for n in frq[i]:
                res.append(n)
                if len(res)==k:
                    return res



        
       
     



        
        