#! usr/bin/python3
# -*- coding = utf-8 -*-


def isValid(s: str) -> bool:
    if not s:
        return True
    stack = []
    left = {'(': ')', '{': '}', '[': ']'}
    for i in s:
        if i in left:
            stack.append(i)
        elif stack:
            top = stack.pop()
            if i != left[top]:
                return False
        else:
            return False
    if stack:
        return False
    else:
        return True


case = "("
print(isValid(case))
