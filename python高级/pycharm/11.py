class A:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        flag = False
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                flag = False
            else:
                if not flag:
                    i += 1
                    nums[i] = nums[j]
                    flag = True
        return nums