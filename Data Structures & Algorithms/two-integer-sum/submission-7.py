class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """ 
        a + b = t
        t - a = b

        [3,4,5,6]    7

         when iterating we know 2 values of 3 required 
        we know a when we are on it but we can know what b is needed to archive t,
         and si if we got such b
        """

        m =  {}
        for i,a in enumerate(nums):
            b = target - a 
            if b in m :
                return [m[b],i]
            m[a] = i
             
        