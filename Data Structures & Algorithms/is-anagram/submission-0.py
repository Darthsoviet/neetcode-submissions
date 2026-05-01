class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def countChars(s):
            d = {}
            for c in s:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] = d[c] + 1
            return d
                    
        d1 = countChars(s)
        d2 = countChars(t)
        return d1 == d2
       