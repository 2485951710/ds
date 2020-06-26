# li=[8,2,2,3,5,8]
# for i in range(len(li)-1,-1,-1):
#     li[i]=li[i]/li[0]
# print(li)
#


class Array:
    def remove(self, nums):
        n = len(set(nums))
        i = 0
        while i < n-1:
            if nums[i] == nums[i + 1]:
                temp = nums[i + 1]
                nums[i + 1:len(nums) - 1] = nums[i + 2:]
                nums[-1] = temp
                continue
            else:
                i += 1
        return i+1

    def removeDuplicates(self, nums):
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow+1



    def removeval(self,nums,val):
        li = [None] * len(nums)
        l=1
        for i in range(len(nums)):
            if nums[i] == val:
                li[:i] = nums[:i]
                li[i:len(nums)-l] = nums[i+1:]
                l += 1
        return  len(nums)-l

    def removeval1(self, nums, val):
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

if __name__ == '__main__':
    a=Array()
    print(a.removeval1([0,1,2,2,3,0,4,2],2))