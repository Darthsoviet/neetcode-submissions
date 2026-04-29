class Solution:



    def canPartition(self, nums: List[int]) -> bool:
        m ={}

        def knap(i,c):
            if m.get((i,c,)) != None:
                return m.get((i,c,))
            
            if i >=len(nums):
                print("bottom")
                return 0
            

            # (1, 3-5 = -2)
            n_cap = c - nums[i]
            zero = knap(i+1, c)

            if nums[i] > c:
                one = knap(i+1, c)

            else:
                one = knap(i+1, n_cap) + nums[i]
            m[(i,c,)] = max(one,zero)
            return m.get((i,c,))
        
        target = 0
        for i in nums:
            target += i
        
        if target % 2 ==1:
            return False
        else:
            target = target // 2
            x = knap(0,target)
            return x == target
        
        






            

            

            
            

            

        