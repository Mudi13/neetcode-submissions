class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}
        for i in range(len(nums)):
            num = nums[i]
            goal = target - num

            if goal in mp:
                return [mp[goal], i]

            mp[nums[i]] = i