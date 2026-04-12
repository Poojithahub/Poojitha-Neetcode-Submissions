class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #this approach uses bucket sort
        count = {} # Creates an empty Dictionary (Hash Map)
        freq = [[] for i in range(len(nums) + 1)]
        # Creates a list of lists (the "Buckets"). 
        # The index of the list represents the frequency. If a number appears 3 times, it goes into freq[3]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # get(num, 0) is a safe way to say: "Give me the current count of this number; if it's not there yet, start at 0.
        for num, cnt in count.items():
            freq[cnt].append(num)
        # for loop logic: Moves data from the Dictionary to the Buckets. 
        # If the number 5 appeared 2 times, we go to index 2 in our freq list and add 5 to it: freq[2].append(5)

        res = []
        # Creates an empty list to store your final answer.
        for i in range(len(freq) - 1, 0, -1):
            # A reverse loop. We start from the very end of the freq list (highest frequency) and move toward the beginning. 
            # Why? Because we want the most frequent items first.
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                # We grab the numbers from the buckets. As soon as our res list has k items in it, we stop and return it.
    
    # ex1: freq[1]= 1, fewq[2]=2, freq[3]=3  -> res[0]= 3, res[1]= 2
    # answer= [3, 2] (in description, incorrect result is given)