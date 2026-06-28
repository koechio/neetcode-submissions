class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = set(nums)
        result = []
        for i in range(len(nums)):
            remaining_number = target - nums[i]
            if remaining_number in nums[i+1:]:
                result.append(i)
                result.append(nums.index(remaining_number, i+1))
                return result

