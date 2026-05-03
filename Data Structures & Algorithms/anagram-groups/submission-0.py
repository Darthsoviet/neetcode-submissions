class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = ord("a")

        def anagram(s):
            d = [0]*26
            for c in s:
                d[ord(c)-x] += 1
            return d
        
        grouping = {}
        for s in strs:
            hsh = str(anagram(s))
            if hsh not in grouping:
                grouping[hsh] = [s]
            else:
                grouping[hsh].append(s)

        return list(grouping.values())



        
        