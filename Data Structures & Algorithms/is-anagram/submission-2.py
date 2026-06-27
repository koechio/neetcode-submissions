class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # loop over the characters in one string
        #initialize a result variable
        # check if it is in the other string
        # if not return false
        if len(s) != len(t):
            return False
        string = t
        for char in s:
            if not char in string:
                return False
            string = t.replace(char, "", 1)
        return True
        