class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        arr = []
        for val,cunnt in cnt.items():
            arr.append([cunnt,val])
        arr.sort()    
        arr= arr[::-1]
        res=[]
        for i in arr:
            res.append(i[1])  
            if len(res)==k:
                return res  



        
        