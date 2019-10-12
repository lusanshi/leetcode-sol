#! usr/bin/python3
# -*- coding = utf-8 -*-


def maxSubArray(nums: list) -> int:
    maxsum = float("-inf")
    tailmax = 0
    for i in nums:
        print(maxsum, tailmax)
        maxsum = max(maxsum, i, i+tailmax)
        tailmax = max(i, i+tailmax)
    return maxsum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = maxSubArray(nums)
print(ans)
