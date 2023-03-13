n = int(input())
e, l, r = ([0 for _ in range(n + 10)] for _ in range(3))

def init():
	global idx
	l[1] = 0
	r[0] = 1
	idx = 2

def insert(k, x):
	global idx
	e[idx] = x
	l[idx] = k
	l[r[k]] = idx
	r[idx] = r[k]
	r[k] = idx
	idx += 1

def remove(k):
	l[r[k]] = l[k]
	r[l[k]] = r[k]

if __name__ == '__main__':

	init()

	insert(0, 1)

	for i in range(2, n+1):
		k, p = map(int, input().split())
		if p: insert(k+1, i)
		else: insert(l[k+1], i)

	m = int(input())
	for x in set([int(input()) for _ in range(m)]):
		remove(x+1)


	i = r[0]
	while i != 1:
		print(e[i], end=' ')
		i = r[i]

