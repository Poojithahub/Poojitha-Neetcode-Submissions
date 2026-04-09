class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # creating a hash map that has val : index

        for i, n in enumerate(nums): # enumerate is built-in function, where i is index and n is value in hashmap
            diff = target - n # difference btw target and number from nums
            if diff in prevMap:  
                return [prevMap[diff], i] # gives index of diff in map, the index of number for whihch we are performing logic(diff)
            prevMap[n] = i