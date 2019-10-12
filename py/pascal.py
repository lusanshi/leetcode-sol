#! usr/bin/python3
# -*- coding = utf-8 -*-


def pascal(numRows: int) -> list:
    if numRows < 1:
        return []
    ans = [[1], ]
    i = 1
    while i < numRows:
        pre = ans[i-1]
        tmp = [1, ]
        for m, n in zip(pre, pre[1:]):
            if not m or not n:
                break
            tmp.append(m+n)
        tmp.append(1)
        ans.append(tmp)
        i += 1
    return ans


print(pascal(100))
