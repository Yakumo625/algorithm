from math import gcd

n, x, y = map(int, input().split())

d = set()
for _ in range(n):
    xx, yy = map(int, input().split())
    a, b = yy - y, xx - x
    a, b = a / gcd(a, b), b / gcd(a, b)
    if a * b > 0: a, b = map(abs, (a, b))
    else: a, b = abs(a), -abs(b)
    d.add((a, b))

print(len(d))