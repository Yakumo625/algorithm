from collections import deque

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(2)]

for i in range(1, n + 1):
    v, w, s = map(int, input().split())
    for r in range(v):
        q = deque()
        for j in range(r, m + 1, v):
            if j > m: break
            if q and j - q[0] > s * v: q.popleft()
            while q and dp[(i - 1) & 1][q[-1]] + (j - q[-1]) // v * w <= dp[(i - 1) & 1][j]: q.pop()
            q.append(j)
            dp[i & 1][j] = dp[(i - 1) & 1][q[0]] + (j - q[0]) // v * w
        
print(dp[n & 1][m])