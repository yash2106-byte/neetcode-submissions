class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if (temp) in mpp:
                return [mpp[temp],i]
            mpp[nums[i]] = i

         