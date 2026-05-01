from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def topDown(h):
            if h >= len(nums):
                return 0

            v = nums[h]
            l = topDown(h+1) 
            r = v+topDown(h+2) 

            return max(l,r)

        return topDown(0)
    
   
        