class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        if n == 0 or n == 1:
            return False
        
        mp = {}
        diff = 0
        
        for i in range(n):
            if nums[i] not in mp:
                mp[nums[i]] = i + 1
            else:
                diff = abs(abs(mp[nums[i]] - 1) - i)
                if diff <= k:
                    return True
                mp[nums[i]] = i + 1
        
        return False
