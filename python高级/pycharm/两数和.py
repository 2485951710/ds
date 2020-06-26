class Solution:
    def twoSum(self,nums,val):
        left = 0
        right = len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == val:
                return [left,right]
                left += 1
                right -= 1
            else:
                if curr > val:
                    right -= 1
                else:
                    left += 1

if __name__ == '__main__':
    s = Solution()
    s.twoSum()