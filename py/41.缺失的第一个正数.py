#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        l = len(nums)
        for i in range(l):
            if nums[i] <= 0 or nums[i] > l:
                nums[i] = 1
        for i in range(l):
            n = abs(nums[i]) - 1
            nums[n] = -abs(nums[n])
        for i in range(l):
            if nums[i] > 0:
                return i + 1
        else:
            return l + 1

# @lc code=end
