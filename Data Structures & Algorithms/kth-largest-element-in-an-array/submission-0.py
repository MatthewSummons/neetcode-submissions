from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        inv_nums = list(map(lambda x: -x, nums))
        heapify(inv_nums)
        for i in range(k-1):
            heappop(inv_nums)
        return -inv_nums[0]
        