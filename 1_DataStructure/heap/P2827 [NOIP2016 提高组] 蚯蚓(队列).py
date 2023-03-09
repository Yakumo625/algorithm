from collections import deque
from math import floor

n, m, q, u, v, t = map(int, input().split())
nums = list(map(int, input().split()))

q1, q2, q3 = deque(reversed(sorted(nums))), deque(), deque()

p = u / v
add_ = 0

for i in range(1, m+1):

	max_ = -1
	max_que = q1
	for que in (q1, q2, q3):
		if que and que[0] + add_ > max_:
			max_ = que[0] + add_
			max_que = que

	if i % t == 0: print(max_, end=' ')

	l = max_que.popleft() + add_
	l1, l2 = floor(p * l) - i*q, l - floor(p * l) - i*q
	q2.append(l1)
	q3.append(l2)

	add_ += q

print()

for i in range(1, n+m+1):

	max_ = -1
	max_que = q1
	for que in (q1, q2, q3):
		if que and que[0] + add_ > max_:
			max_ = que[0] + add_
			max_que = que

	if i % t == 0: print(max_, end=' ')
	max_que.popleft()




	

