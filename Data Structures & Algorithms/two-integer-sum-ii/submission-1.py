class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        # here l=0, r= len(numbers)-1= 4-1=3

        while l < r:
            curSum = numbers[l] + numbers[r]
            # since given array is in ascending order, if current sum > target, then move to before number of r.
            # if current sum < target, increase l i.e. move to next number after l
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else: # when currsum=target
                return [l + 1, r + 1] # in ex1, index 1 & 2 has sum that matches target 3. in result, we returned indexes, not values
                # since in questions, its given as 1-inderexed, we are adding 1 to both indexes at end
        return []