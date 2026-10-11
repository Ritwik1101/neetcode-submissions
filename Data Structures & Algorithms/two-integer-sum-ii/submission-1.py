class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        n=len(numbers)
        r=n-1
        while l<r:
            currsum=numbers[l]+numbers[r]
            if currsum > target:
                r-=1    

            elif curr < target:
                l+=1
            else:
                return [i+1,j+1]



             

        