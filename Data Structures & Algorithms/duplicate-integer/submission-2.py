class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {} 
        duplicate = False
        for num in nums:
            if num in numbers:
                duplicate = True
            else:
               numbers[num] = num 
        return duplicate

