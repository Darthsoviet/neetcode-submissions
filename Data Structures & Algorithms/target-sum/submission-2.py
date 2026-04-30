class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.knap(0,target, nums, {})

    def knap(self,i , w , nums, mem):
        if mem.get((i,w,)):
            return mem.get((i,w,))
        if i >= len(nums) and w == 0:
            return 1
        if i >= len(nums):
            return 0
        v = nums[i]
       
        sub = self.knap( i + 1, w - v , nums, mem)
        add = self.knap( i + 1, w + v , nums, mem)
        mem[(i,w,)] = add + sub
        return mem.get((i,w,))




        