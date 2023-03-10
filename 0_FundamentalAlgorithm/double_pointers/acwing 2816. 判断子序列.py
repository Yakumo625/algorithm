n, m = map(int, input().split())
a, b = (list(map(int, input().split())) for _ in range(2))

i = j = 0

while i < n: and j < m:
	if a[i] == b[j] : i += 1
	j += 1
if i == n: print('Yes')
else: print('No')