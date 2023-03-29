n, m = map(int, input().split())
v, w = [0], [0]
dp = [0] * (m + 1)

for _ in range(n):
    vi, wi, s = map(int, input().split())
    i = 1
    while i <= s:
        v.append(i * vi)
        w.append(i * wi)
        s -= i
        i <<= 1
    if s > 0:
        v.append(s * vi)
        w.append(s * wi)

for i in range(1, len(v)):
    for j in range(m, v[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - v[i]] + w[i])

print(dp[m])
