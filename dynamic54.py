#! usr/bin/python3


def climbStairs(n: int) -> int:
    ans = 0
    for x in range(n+1):
        for y in range(n//2 + 1):
            if x+2*y == n:
                ans += cmbt(x, y)
    return ans


def climbStairs1(n: int) -> int:
    dp = [1, 1, 2]
    if n < len(dp):
        return dp[n]
    else:
        for i in range(3, n+1):
            dp[-1], dp[-2] = dp[-1]+dp[-2], dp[-1]
        return dp[-1]


def cmbt(x, y) -> int:
    a, b = 1, 1
    while y > 0:
        a *= x+y
        b *= y
        y -= 1
    return a//b


n = 500
print("fib=", climbStairs1(n))
# print("排列组合",climbStairs(n))

# print(pmt(5))
