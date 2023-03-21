from copy import deepcopy

n = int(input())

def turn(x, y):
	dxy = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
	for dx, dy in dxy:
		i, j = x + dx, y + dy
		if i < 0 or i > 4 or j < 0 or j > 4: continue
		state[i][j] ^= 1

for _ in range(n):
	state = [[int(i) for i in input()] for _ in range(5)]
	backup = deepcopy(state)

	ans = 25
	for init in range(32): # 00000~11111
		cnt = 0

		for j in range(5):
			if init >> (4 - j) & 1:
				cnt += 1
				turn(0, j)

		for i in range(4):
			for j in range(5):
				if not state[i][j]:
					cnt += 1
					turn(i+1, j)

		if all(state[4]): ans = min(ans, cnt)
		state = deepcopy(backup)

	print(-1 if ans > 6 else ans)
	if _ != n-1: input()