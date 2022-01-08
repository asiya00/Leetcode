def trailingZeroes(n: int) -> int:
    # count = 0
    # while n >= 5:
    #     n = n//5
    #     count += n
    # return count
    if n < 5:
        return 0
    if n >= 5:
        return n // 5 + trailingZeroes(n // 5)


print(trailingZeroes(15))
