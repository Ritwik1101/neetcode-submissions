class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=0
        ml=0
        for i in s:
            if i not in seen:
                seen.add(i)
                l+=1
                ml=max(ml,l)
            else:
                l=-1
                seen.remove(i)  
        return ml          

        