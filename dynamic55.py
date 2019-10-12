#! usr/bin/python3


def maxProfit(prices: list) -> int:
    maxp, high, low = 0, 0, 0
    ans = []
    pre = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > pre:
            if pre < low or high == low:
                ans.append(maxp)
                low = pre
                high = prices[i]
            elif high < prices[i]:
                high = prices[i]
            maxp = high - low
        pre = prices[i]
    ans.append(maxp)
    return max(ans)


def maxProfit1(prices: list) -> int:
    cost, profit = float("+inf"), 0
    for price in prices:
        cost = min(price, cost)
        profit = max(price - cost, profit)
    return profit


p = [7, 1, 5, 3, 6, 4]

print(maxProfit1(p), maxProfit(p))
