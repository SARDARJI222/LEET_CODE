# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n ==1:
#             return 1
#         if n== 2:
#             return 2
#         return self.climbStairs(n-2) +self.climbStairs(n-1)
# here time limit exceed 
    
    
    
    class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        if n== 2:
            return 2
        # return self.climbStairs(n-2) +self.climbStairs(n-1)
        two_back=2
        one_back=1
        for i in range(3,n+1):
            ret = two_back + one_back
            two_back=one_back
            one_back=ret
        return ret
