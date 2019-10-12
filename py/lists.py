#! usr/bin/python3
# -*- coding = utf-8 -*-


def threeSum(nums: list) -> list:
    nums.sort()
    ans = []
    for index, element in enumerate(nums):
        if element > 0:
            break
        if index > 0 and nums[index] == nums[index-1]:
            continue
        tmp = nums[index+1:]
        left, right = 0, len(tmp)-1
        while left < right:
            if tmp[left] + tmp[right] > -element:
                right -= 1
                while left < right and tmp[right] == tmp[right+1]:
                    right -= 1
            elif tmp[left] + tmp[right] < -element:
                left += 1
                while left < right and tmp[left] == tmp[left-1]:
                    left += 1
            else:
                ans.append([element, tmp[left], tmp[right]])
                left += 1
                while left < right and tmp[left] == tmp[left-1]:
                    left += 1
                right -= 1
                while left < right and tmp[right] == tmp[right+1]:
                    right -= 1
    return ans


def setZeroes(matrix: list) -> None:
    # dic = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))
    #        if matrix[i][j] == 0]
    rows, cols = [], []
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == 0:
                if i not in rows:
                    rows.append(i)
                if j not in cols:
                    cols.append(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in rows or j in cols:
                matrix[i][j] = 0


tcase = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
setZeroes(tcase)
print(tcase)
