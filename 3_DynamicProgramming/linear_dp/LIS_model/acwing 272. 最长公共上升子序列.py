n = int(input())
a, b = ([0] + list(map(int, input().split())) for _ in range(2))

f = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    maxv = 1
    for j in range(1, n + 1):
        f[i][j] = f[i - 1][j]
        if a[i] == b[j]: f[i][j] = max(f[i][j], maxv)
        if a[i] > b[j]: maxv = max(maxv, f[i - 1][j] + 1)

print(max(f[n]))