class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i in range(len(nums)):
            dictionary[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dictionary and dictionary[complement] != i:
                return [i, dictionary[complement]]