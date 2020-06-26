class Solution:
    def movezeros(self,nums):
        slow = 0
        fast = 0
        while fast < len(nums)-1:
            if nums[fast] == 0:
                nums[slow] = nums[fast+1]
                fast += 1
            else:
                slow += 1
                fast += 1
                nums[slow] = nums[fast]
        for i in range(slow+1,len(nums)):
            nums[i] = 0
        return nums

    def movezeros(self,nums):
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == 0:
                nums[slow] = nums[fast+1]
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
        return nums

    def removeElement(self, nums, val):
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
        return i+1



if __name__ == '__main__':
    m =Solution()
    print(m.removeDuplicates([]))
    print(m.removeDuplicates([0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5]))
    print(m.removeDuplicates([0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5]))
