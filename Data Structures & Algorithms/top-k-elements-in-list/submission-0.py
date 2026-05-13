class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        count_to_val = [ [] for _ in nums ]
        for ky, v in count.items():
            count_to_val[v - 1].append(ky)
        
        res, ptr, walk = [], len(nums) - 1, k
        while ptr >= 0 and len(res) < k:
            if count_to_val[ptr - 1]:
                res += count_to_val[ptr - 1][:walk]
                walk -= len(count_to_val[ptr - 1])
            ptr -= 1
        
        return res