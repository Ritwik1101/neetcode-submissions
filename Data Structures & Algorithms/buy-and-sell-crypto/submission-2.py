class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0
        r=len(prices)-1
        mpro =0
        while l<r:
            if prices[l]<prices[r]:
                mpro = max(mpro,prices[r]-prices[l])
                l+=1
            r-=1
        return mpro            

        


                
            
        