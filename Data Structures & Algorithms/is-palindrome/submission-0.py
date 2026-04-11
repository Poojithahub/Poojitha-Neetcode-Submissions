class Solution: # class
    def isPalindrome(self, s: str) -> bool: 
        # isPalindrome: function,  self- std word in a fucntion, s: str -> expectes string input, bool- output will be true/false
        newStr = '' # creates a new string
        for c in s:
            if c.isalnum(): 
                # isalnum- It returns True if all characters in a string are alphanumeric (meaning only letters and numbers); otherwise, it returns False.
                newStr += c.lower()
        return newStr == newStr[::-1] # newStr[::-1] - reverses the string.


# T: O(n)
# S: O(n)