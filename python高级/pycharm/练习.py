# -*- coding:utf-8 -*-
def removeDuplicated(nums):
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1

def removeval(nums, val):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        else:
            fast += 1
    return slow

# print(removeval([0,1,2,2,3],2))

print(removeDuplicated([1,2,3,3,5,6,7]))