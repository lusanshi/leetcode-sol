#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        # if x == 0:
        #     return 0
        # if x < 4:
        #     return 1
        left, right = 0, x//2 + 1
        while left*left != x:
            while right*right != x:
                if right - left == 1:
                    return left
                mid = (left+right)//2
                if mid*mid < x:
                    left = mid
                elif mid*mid > x:
                    right = mid
                else:
                    return mid
            return right
        return left


