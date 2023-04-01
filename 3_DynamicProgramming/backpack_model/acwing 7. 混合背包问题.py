n, m = map(int, input().split())

dp = [0] * (m + 1)

for _ in range(n):
    v, w, s = map(int, input().split())
    
    if s == -1:
        for j in range(m, v - 1, -1):
            dp[j] = max(dp[j], dp[j - v] + w)
    elif s == 0:
        for j in range(v, m + 1):
            dp[j] = max(dp[j], dp[j - v] + w)
    else:
        vs, ws, i = [0], [0], 1
        while i <= s:
            vs.append(i * v)
            ws.append(i * w)
            s -= i
            i <<= 1
        if s > 0:
            vs.append(s * v)
            ws.append(s * w)
        
        for i in range(1, len(vs)):
            for j in range(m, vs[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - vs[i]] + ws[i])

print(dp[m])