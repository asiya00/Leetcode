import math
def climbStairs(n: int) -> int:
    n = n+1
    p1 = (1 + math.sqrt(5))**(n)
    p2 = (1 - math.sqrt(5))**(n)
    b = (p1 - p2)/(2**n * math.sqrt(5))
    return int(b)


n = 2
print(climbStairs(n))
