class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cunt = Counter(nums)
        freq= [[] for _ in range(len(nums)+1)]  
        for val,cnt in cunt.items():
            freq[cnt].append(val)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for kk in freq[i]:
                res.append(kk)
                if len(res)==k:
                    return res 



        
       
     



        
        