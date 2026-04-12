class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

# r-> 0 to 6 (so we traverse for loop 7 times)
# when r=3, l=max(0+1, 0)=1
# mp[z]= 0, mp[x]=1, mp[y]=2
# res-> max(0, 0-0+1)=1, max(1, 1-0+1)=2, max(2, 2-0+1)=3, 