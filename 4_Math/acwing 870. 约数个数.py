from collections import defaultdict as ddict

mod = int(1e9) + 7
d = ddict(int)

for _ in range(int(input())):
    n = int(input())
    for i in range(2, n):
        if i * i > n: break
        while n % i == 0:
            n //= i
            d[i] += 1
    if n > 1: d[n] += 1

res = 1
for y in d.values():
    res = res * (y + 1) % mod

print(res)