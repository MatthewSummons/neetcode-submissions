class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(len(nums) - 1):
            prefix[i + 1] = nums[i] * prefix[i]
        
        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i]
        
        return ans
