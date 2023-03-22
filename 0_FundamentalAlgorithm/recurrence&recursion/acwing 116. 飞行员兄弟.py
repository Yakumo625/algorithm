from copy import deepcopy as dcp

state = [[int(i=='-') for i in input()] for _ in range(4)]
backup = dcp(state)

def turn(i, j):
	for k in range(4):
		state[k][j] ^= 1
		state[i][k] ^= 1
	state[i][j] ^= 1

ans, ansop = 16, []
for st in range(65536):

	op = []
	for i in range(4):
		for j in range(4):
			if st >> (15-(4 * i + j)) & 1:
				turn(i, j)
				op.append((i + 1, j+1))

	if all(map(all, state)) and ans > len(op): ans, ansop = len(op), op[:]
	state = dcp(backup)

print(ans)
for i, j in ansop:
	print(i, j)