class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
         counter = Counter(nums1)
         result = []
         for i in nums2:
             k = counter.get(i)
             if k!=None and k > 0:
                 counter[i]-=1
                 result.append(i)
        
         return result
