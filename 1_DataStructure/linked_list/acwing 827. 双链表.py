'''
init status:

    ____     -------->     ____   
  /      \\              /      \
 |    0    |            |   1    |
  \\______/  <--------  \\______/ 

'''

N = int(1e5) + 10
e = [0 for _ in range(N)]
l = [0 for _ in range(N)]
r = [0 for _ in range(N)]

def init():
	global idx
	r[0] = 1
	l[1] = 0
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

	n = int(input())
	for _ in range(n):
		op = input().split()
		if op[0] == 'L': insert(0, int(op[1]))
		elif op[0] == 'R': insert(l[1], int(op[1]))
		elif op[0] == 'D': remove(int(op[1]) + 1)
		elif op[0] == 'IL': insert(l[int(op[1]) + 1], int(op[2]))
		elif op[0] == 'IR': insert(int(op[1]) + 1, int(op[2]))

	i = r[0]
	while i != 1:
		print(e[i], end=' ')
		i = r[i]
