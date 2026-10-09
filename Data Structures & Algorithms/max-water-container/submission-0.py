class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        val=0
        while l<r:
            if heights[l]>heights[r]:
                val=max(val,min(heights[l],heights[r])*(r-l))
                r-=1
            elif  heights[r]>heights[l]:
                val=max(val,min(heights[l],heights[r])*(r-l))
                l+=1   
            else:
                val=max(val,min(heights[l],heights[r])*(r-l))
                l+=1
                r-=1
        return val        


            
        