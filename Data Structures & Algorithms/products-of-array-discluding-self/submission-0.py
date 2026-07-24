class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        prefix[0] = 1
        for i in range(1, n, 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix = [1] * n
        suffix[n-1] = 1
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        ans = [1] * n
        for i in range(0, n, 1):
            ans[i] = prefix[i] * suffix[i]

        return ans
