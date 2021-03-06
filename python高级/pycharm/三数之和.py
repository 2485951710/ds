from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        for i in range(1, len(nums)-1):
            slow = 0
            fast = len(nums) - 1
            while slow < i or i < fast:
                if nums[slow] + nums[fast] + nums[i] < 0:
                    slow += 1
                elif nums[slow] + nums[fast] + nums[i] > 0:
                    fast -= 1
                else:
                    if [nums[slow], nums[i], nums[fast]] not in l:
                        l.append([nums[slow], nums[i], nums[fast]])
                    slow += 1
                    fast -= 1
            return l
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return res