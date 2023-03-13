# custom method

m = int(input())
head, tail = 0, -1
q = [0 for _ in range(m + 10)]

for _ in range(m):
	op = input().split()
	if op[0] == 'push':
		tail += 1
		q[tail] = int(op[1])
	elif op[0] == 'pop':
		head += 1
	elif op[0] == 'empty':
		print('YES' if head > tail else 'NO')
	else:
		print(q[head])



# builtin method
# from collections import deque

# m = int(input())
# q = deque()

# for _ in range(m):
# 	op = input().split()
# 	if op[0] == 'push': q.append(int(op[1]))
# 	elif op[0] == 'pop': q.popleft()
# 	elif op[0] == 'empty': print('NO' if q else 'YES')
# 	else: print(q[-1])


