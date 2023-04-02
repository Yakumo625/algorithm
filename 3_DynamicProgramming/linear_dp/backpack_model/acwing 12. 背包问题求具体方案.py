# n, m = map(int, input().split())
# v, w = zip((0, 0), *(map(int, input().split()) for _ in range(n)))
# dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

# dp[0][0] = 0
# for i in range(1, n + 1):
#     for j in range(m + 1):
#         dp[i][j] = dp[i - 1][j]
#         if j >= v[i]: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i])

# res = max(dp[n])
# anss = []
# for j in range(m + 1):
    
#     if dp[n][j] == res:
#         i, ans = n, []
#         while i > 0:
#             if j >= v[i] and dp[i][j] == dp[i - 1][j - v[i]] + w[i]:
#                 ans.append(i)
#                 j -= v[i]
#             i -= 1
#         anss.append(ans[::-1])

# anss.sort()
# if anss[0] == [237,247,283,286,287,291,299,300]:
#     test1 = [3,4,5,7,10,11,167,237]
#     test2 = [237,247,283,286,287,291,299,300]
#     print(sum([w[t] for t in test1]),sum([v[t] for t in test1]),sum([w[t] for t in test2]), sum([v[t] for t in test2]))
#     print(sum([t == 500 for t in dp[n]]))
# print(*anss[0], sep=' ')

n, m = map(int ,input().split())
v, w = zip((0, 0), *(map(int, input().split()) for _ in range(n)))

dp = [[0] * (m + 1) for _ in range(n + 2)]

for i in range(n, 0, -1):
    for j in range(m + 1):
        dp[i][j] = dp[i + 1][j]
        if j >= v[i]: dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - v[i]] + w[i])

j = m
for i in range(1, n + 1):
    if j >= v[i] and dp[i][j] == dp[i + 1][j - v[i]] + w[i]:
        print(i, end=' ')
        j -= v[i]