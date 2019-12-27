#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ret = [0] * length
        r = [0] * length
        l = [0] * length
        index, m = 0, 1
        for i in nums:
            l[index] = m
            m = m*i
            index += 1
        index, m = length-1, 1
        for i in nums[::-1]:
            r[index] = m
            m = m*i
            index -= 1
        for i in range(length):
            ret[i] = r[i]*l[i]

        return ret
# @lc code=end

