class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we have methoods- brute force, sorting, hash set
        # always prefer latest best method to reduce space & time complexity
        # below is hashset
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # method: hash set length
        # return len(set(nums)) < len(nums)