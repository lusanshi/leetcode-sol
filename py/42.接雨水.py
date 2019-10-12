#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        temp = None
        sumValue = 0
        maxValue = max(height)
        count = height.count(maxValue)
        for h in height:
            if h!= maxValue:
                if not temp or h > temp:
                    temp = h
                else:
                    sumValue += temp - h
            elif count > 1:
                temp = h
                count -= 1
            else:
                break
        temp = 0
        for h in height[::-1]:
            if h!= maxValue:
                if not temp or h > temp:
                    temp = h
                else:
                    sumValue += temp - h
            else:
                break
        return sumValue

