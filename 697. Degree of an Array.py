class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 1
                first[num] = i
                last[num] = i
            else:
                count[num] += 1
                last[num] = i

        max_count = max(count.values())
        result = len(nums)
        for num, cnt in count.items():
            if cnt == max_count:
                result = min(result, last[num] - first[num] + 1)
        return result
