from heapq import heapify, nsmallest, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.maxHeap = list(map(lambda x : -x, nums))
        
        heapify(self.maxHeap)
        print (self.maxHeap)
        
        

        

    def add(self, val: int) -> int:
        heappush(self.maxHeap, -val)
        return -nsmallest(self.k, self.maxHeap)[-1]
        
