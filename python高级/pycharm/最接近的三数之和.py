def threeSumClosest(nums, target):
    nums.sort()
    min = abs(nums[0] + nums[1] + nums[2])
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        lefe = i + 1
        right = len(nums)-1
        while lefe < right:
            sum = nums[i] + nums[lefe]+nums[right]
            if abs(sum - target) < min:
                min = abs(sum - target)
                res = sum
            if sum > target:
                right -= 1
            elif sum < target:
                lefe += 1
            else:
                return sum