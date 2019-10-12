#! usr/bin/python3
# -*- coding = utf-8 -*-


def missingNumber(nums: list) -> int:
    n = len(nums)
    return n*(n+1)//2 - sum(nums)


case = [9, 6, 4, 2, 3, 5, 7, 1, 8]
print(missingNumber(case))
