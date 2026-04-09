class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26  #creating an array of 26 columns(as we have 26 alpahabets)
        for i in range(len(s)): 
            count[ord(s[i]) - ord('a')] += 1 #ord means odinal-> ord('a') gives ascii value= 97, so 97-97=0
            count[ord(t[i]) - ord('a')] -= 1 #ord() converts char to ASCII/Unicode integer

        for val in count:
            if val != 0: #checking if any value in count[] array has 0. if any value is 0, then its not a anagram
                return False
        return True
        