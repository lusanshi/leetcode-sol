#! usr/bin/python3
# -*- coding = utf-8 -*-
from RuntimeDecorate import runtime

data = {}


@runtime
def rob(nums: list) -> int:
    if not nums:
        return 0
    l = len(nums)
    if l == 1:
        return nums[0]
    elif l == 2:
        return max(nums[0], nums[1])
    elif l == 3:
        return max(nums[1], nums[0] + nums[2])
    if l not in data:
        data[l] = max(nums[0] + rob(nums[2:]), nums[1] + rob(nums[3:]))
    return data[l]


@runtime
def rob2(nums: list) -> int:

    pre = 0
    cur = 0

    for num in nums:
        print("cur:%d,pre:%d" % (cur, pre))
        tmp = cur
        cur = max(pre+num, cur)
        pre = tmp
    return cur


q0 = [1, 1, 1, 1]
q1 = [2, 7, 9, 3, 1]
q = [155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66,
     134, 26, 25, 205, 239, 85, 146, 73, 55, 6, 122, 196, 128, 50, 61, 230, 94,
     208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212,
     241, 242, 157, 79, 133, 66, 36, 165]

ans = rob(q)
