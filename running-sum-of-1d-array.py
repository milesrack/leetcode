class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:

        nums_sum = []

        for i in range(len(nums)):

            nums_sum.append(sum(nums[:i+1]))

        return nums_sum

