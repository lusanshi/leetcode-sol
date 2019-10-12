#!/usr/bin/python3
def getnext(s: str) -> list:
    slen = len(s)
    arr = [0]*slen

    for i in range(1, slen-1):
        temp = list(s[:i+1])
        max = 0
        print(temp)
        for k in range(i+1):
            if temp[:k] == temp[-k:]:
                max = k

        arr[i+1] = max
        temp.clear()

    return arr


a = "aac"
b = "ababcaabc"
c = "abbabbbabaa"
print(getnext(c))
