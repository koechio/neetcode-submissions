class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        for char in s:
            countS[char] = 1+ countS.get(char,0)
        for char in t:
            countT[char] =  1+ countT.get(char,0)
        for char in countS:
            if not countS[char] == countT.get(char):
                return False
        return True

        
        