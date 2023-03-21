start, end = ([1 if c == '*' else 0 for c in input()] for _ in range(2))

cnt = 0
for i in range(len(start) - 1):
	if start[i] != end[i]:
		start[i] ^= 1
		start[i + 1] ^= 1
		cnt += 1

print(cnt)