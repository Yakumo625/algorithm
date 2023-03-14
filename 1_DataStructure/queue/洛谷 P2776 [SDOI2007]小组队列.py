from collections import deque

n, m = map(int, input().split())
d = {i : j for i, j in enumerate(map(int, input().split()), start=0)}
groups = [deque() for _ in range(m + 10)]

T = int(input())

q = deque()
for _ in range(T):
	input_ = input().split()
	op = input_[0]

	if op == 'push':
		num = int(input_[1])
		group_num = d[num]
		if not groups[group_num]: q.append(group_num)
		groups[group_num].append(num)

	elif op == 'pop':
		head = q[0]
		print(groups[head].popleft())
		if not groups[head]: q.popleft()