from heapq import heapify, nsmallest, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        heapify(nums)
        self.minHeap = nums
        while (len(self.minHeap) > k):
            heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if (len(self.minHeap) > self.k):
            heappop(self.minHeap)
        return self.minHeap[0]