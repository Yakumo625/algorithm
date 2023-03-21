T = int(input())

for _ in range(T):
	n = int(input())
	str1 = [c for c in input()]
	str2 = str1[:]
	op1, op2 = [], []

	for i in range(n-1):

		if str1[i] == 'W':
			op1.append(i+1)
			str1[i] = 'B'
			if str1[i + 1] == 'W':
				str1[i + 1] = 'B'
			else: 
				str1[i + 1] = 'W'

		if str2[i] == 'B':
			op2.append(i+1)
			str2[i] = 'W'
			if str2[i + 1] == 'W':
				str2[i + 1] = 'B'
			else:
				str2[i + 1] = 'W'

	if str1[-1] == 'B':
		print(len(op1))
		if op1: print(*op1)
	elif str2[-1] == 'W':
		print(len(op2))
		if op2: print(*op2)
	else:
		print(-1)