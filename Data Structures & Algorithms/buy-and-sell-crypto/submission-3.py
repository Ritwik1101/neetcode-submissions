class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l =0
        r=1
        mpro =0
        while r<len(prices):
            if prices[l]<prices[r]:
                mpro = max(mpro,prices[r]-prices[l])
               
            else:
                l=r
            r+=1    
        return mpro            

        


                
            
        