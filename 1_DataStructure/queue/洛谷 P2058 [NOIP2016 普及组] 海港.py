from collections import deque
from collections import defaultdict as ddict

n = int(input())
q = deque()
tq = ddict(lambda: deque())
exist = [0] * 300005

ans = 0

for _ in range(n):
	t, k, *nums = map(int, input().split())
	q.append(t)
	for num in nums:
		tq[t].append(num)
		if not exist[num]: ans += 1
		exist[num] += 1
	while t - q[0] >= 86400:
		for num in tq[q.popleft()]:
			exist[num] -= 1
			if not exist[num]: ans -= 1
	print(ans)





