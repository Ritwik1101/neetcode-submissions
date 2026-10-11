class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmp={val:idx for idx,val in enumerate(nums)}
        for i in range(len(nums)):
            res =  target-nums[i]
            if res in hashmp:
                return [i,hashmp[res]]