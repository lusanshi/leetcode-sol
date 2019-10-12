#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        m_left, m_right, n_left, n_right = 0, len1 - 1, 0, len2 - 1

(n//2 + (n+1)//2)/2
