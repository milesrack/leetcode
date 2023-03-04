class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        start = 0
        minFound = False
        minStart = 0
        maxFound = False
        maxStart = 0
        for i in range(start, len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                minFound, maxFound = False, False
                start = i + 1
            if nums[i] == minK:
                minFound = True
                minStart = i
            if nums[i] == maxK:
                maxFound = True
                maxStart = i
            if minFound and maxFound:
                count += min(minStart, maxStart) - start + 1
        return count
