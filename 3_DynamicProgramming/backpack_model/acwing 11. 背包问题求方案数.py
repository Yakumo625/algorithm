n, m = map(int, input().split())

f = [0] + [float('-inf') for _ in range(m)]
g = [1] + [0] * m

for i in range(n):
    v, w = map(int, input().split())
    for j in range(m, v - 1, -1):
        maxv, cnt = max(f[j], f[j - v] + w), 0
        if maxv == f[j]: cnt = g[j]
        if maxv == f[j - v] + w: cnt += g[j - v]
        f[j], g[j] = maxv, cnt % (int(1e9) + 7)

res = sum_ = 0
for i in range(m + 1):
    if f[i] > f[res]: res = i
for i in range(m + 1):
    if f[i] == f[res]: sum_ += g[i]
print(sum_ % (int(1e9) + 7))