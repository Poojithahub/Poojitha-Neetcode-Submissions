class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)   # If this key doesn't exist yet, automatically create an empty [] list for me."
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) #tuple is Immutable(doesn't change)
        return list(res.values())