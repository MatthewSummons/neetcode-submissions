from heapq import heapify, nlargest, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        heapify(nums)
        self.minHeap = nums
        while (len(self.minHeap) > k + 1):
            heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if (len(self.minHeap) > self.k + 1):
            heappop(self.minHeap)
        return nlargest(self.k, self.minHeap)[-1]
        
