N = int(input())
h = [int(input()) for _ in range(N)]
stack = []
res = []

for i in range(N, 0, -1):
	while stack and h[stack[-1]-1] <= h[i-1]: stack.pop()
	res.append(stack[-1] if stack else 0)
	stack.append(i)

print(*res[::-1], sep='\n')
