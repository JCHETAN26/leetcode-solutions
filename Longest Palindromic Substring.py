class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l,r):
            while(l>=0 and r <len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        res=""
        for i in range(len(s)):
            t = helper(i,i)
            if len(t)>len(res): res = t
            t= helper(i,i+1)
            if len(t)>len(res): res = t
        return res      
