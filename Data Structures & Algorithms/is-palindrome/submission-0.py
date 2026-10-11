class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalpha() :
                res+=i.lower()
        return res==res[::-1]        
        