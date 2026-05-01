from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def topDown(h):
            if h >= len(nums):
                return 0

            v = nums[h]
            l = v+ topDown(h+2) 
            r = v+topDown(h+3) 

            return max(l,r)

        return max(topDown(0),topDown(1))
    
   
        