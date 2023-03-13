m = int(input())
stack = [0 for _ in range(m + 10)]
head = -1

for _ in range(m):
	op = input().split()
	if op[0] == 'push':
		head += 1
		stack[head] = int(op[1])
	elif op[0] == 'query':
		print(stack[head])
	elif op[0] == 'pop':
		head -= 1
	elif op[0] == 'empty':
		print('YES' if head == -1 else 'NO')