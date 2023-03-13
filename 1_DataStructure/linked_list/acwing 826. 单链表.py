N = int(1e5) + 10
e = [0 for _ in range(N)]
ne = [0 for _ in range(N)]

def init():
	global head, idx
	head, idx = -1, 0

def add_to_head(x):
	global head, idx
	e[idx] = x
	ne[idx] = head
	head = idx
	idx += 1

def insert(k, x):
	global idx
	e[idx] = x
	ne[idx] = ne[k]
	ne[k] = idx
	idx += 1

def remove(k):
	ne[k] = ne[ne[k]]


if __name__ == '__main__':
	init()

	n = int(input())
	for _ in range(n):
		op = input().split()
		if op[0] == 'H':
			add_to_head(int(op[1]))
		elif op[0] == 'I':
			insert(int(op[1]) - 1, int(op[2]))
		else:
			if int(op[1]) == 0: head = ne[head]
			else: remove(int(op[1]) - 1)

	i = head
	while i != -1:
		print(e[i], end=' ')
		i = ne[i]
