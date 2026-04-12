class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: # (2-1=1 is not in numset, so 2 is start of a sequence)
                # here we are checking if the number in array is the start of a sequence
                # if num-1 exists in numset, then its not start of a sequence
                # sequence= [2, 3, 4, 5]; [10]; [20]: here 2, 10 & 20 are start fo sequences
                length = 1
                while (num + length) in numSet: # (2+1=3 in numset, 2+2=4 in numset, 2+3=5 in numset, 2+4=6 not in numset-> so exit while loop)
                    length += 1 # length= 1+1=2, 2+1=3, 3+1=4
                longest = max(length, longest) # considering longest variable for other sequences, to get max(length) from all sequences in array
        return longest

# for sequence [2, 3, 4, 5], length & longest =4; for [10], length= 1; for [20], length= 1