from collections import defaultdict as ddict
from collections import deque

m, n = map(int, input().split())
words = list(map(int, input().split()))
d = ddict(int)
mem = deque()

cnt = 0
for word in words:
	if not d[word]:
		if len(mem) < m:
			mem.append(word)
			d[word] += 1
		else:
			d[mem.popleft()] -= 1
			d[word] += 1
			mem.append(word)
		cnt += 1
		
print(cnt)
