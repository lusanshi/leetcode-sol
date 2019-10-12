#!/usr/bin/python3
def strStr(haystack: str, needle: str) -> int:
    i, j, h, n = 0, 0, len(haystack), len(needle)
    if h < n or (h == n and haystack != needle):
        return -1
    if n == 0:
        return 0
    nextarr = [0]*n
    for var in range(1, n-1):
        temp = list(needle[:var+1])
        max = 0
        for k in range(var+1):
            if temp[:k] == temp[-k:]:
                max = k
        nextarr[var+1] = max
        temp.clear()
    while i < h:
        temp = i
        print('i1 =', i)
        print('j1 =', j)
        while j < n and i < h and needle[j] == haystack[i]:
            i += 1
            j += 1
            print('i2 =', i)
            print('j2 =', j)
        if j == n:
            return i - j
        if temp == i and j == 0:
            i += 1
        j = nextarr[j]
    return -1


a = "ababaabbbbababbaabaaabaabbaaaabbabaabbbbbbabbaabbabbbabbbbbaaabaababbbaab
bbabbbaabbbbaaabbababbabbbabaaabbaabbabababbbaaaaaaababbabaababaabbbbaaab
bbabb"
b = "abbabbbabaa"
print(strStr(a, b))
