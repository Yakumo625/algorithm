n = int(input())
cps = [(int(input()), i + 1) for i in range(n)]

ans = []
stack = []
cps = cps[::-1]

for cp in cps:
	while stack and stack[-1][0] <= cp[0]: stack.pop()
	if stack: ans.append(stack[-1][1])
	else: ans.append(0)
	stack.append(cp)

print(*ans[::-1], sep='\n')

