#! usr/bin/python3
# -*- coding = utf-8 -*-
from RuntimeDecorate import runtime


def fizzBuzz(n: int):
    ans = []
    while n > 0:
        if n % 15 == 0:
            ans.append("FizzBuzz")
        elif n % 3 == 0:
            ans.append("Fizz")
        elif n % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(n))
        n -= 1
    ans.reverse()
    return ans


def isPrime(i, nums):
    for p in nums:
        if p > pow(i, 0.5):
            break
        if i % p == 0:
            return False
    return True


@runtime
def countPrimes1(n: int) -> int:
    if n < 3:
        return 0
    i = 3
    dic = []
    count = 1
    while i < n:
        if isPrime(i, dic):
            dic.append(i)
            count += 1
        i += 2
    return count


@runtime
def countPrimes(n: int) -> int:
    if n < 3:
        return 0
    i, count = 2, 0
    dic = list(range(2, n))
    while i < pow(n, 0.5):
        k = i*i
        while k < n:
            dic[k-2] = None
            k += i
        i += 1
        while not dic[i-2]:
            i += 1
    for num in dic:
        if num:
            count += 1
    return count


func = [countPrimes1, countPrimes]
for f in func:
    f(1000000)
# print(fizzBuzz(15))


def romanToInt(s: str) -> int:
    intnum, key = 0, 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for r in s[::-1]:
        if dic[r] >= key:
            intnum += dic[r]
        else:
            intnum -= dic[r]
        key = dic[r]
    return intnum

# s = "IV"
# print(romanToInt(s))
