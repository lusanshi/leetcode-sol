#! usr/bin/python3
# -*- coding = utf-8 -*-


def hammingDistance(x: int, y: int) -> int:
    z = str(bin(x ^ y))
    count = 0
    for s in z:
        if s == "1":
            count += 1
    return count


print(hammingDistance(1, 4))
