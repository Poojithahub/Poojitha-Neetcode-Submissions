class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we have methoods- brute force, sorting, hash set
        # always prefer latest best method to reduce space & time complexity
        # below is hashset method
        seen = set()  # here seen is a hashset
        for num in nums:
            if num in seen:
                return True # return true if found a duplicate
            seen.add(num) # add to hashset if u dont find a duplicate in seen hashset
        return False # if found no duplicates in hashset, then it comes out of if loop and false will be retunred

        # method: hash set length
        # return len(set(nums)) < len(nums)

        # complexities:
        # time: O(n)
        # space: O(n)
