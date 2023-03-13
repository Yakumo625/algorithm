n = int(input())
nums = list(map(int, input().split()))
stack = []

for num in nums:
	while stack and stack[-1] >= num:
		stack.pop()
	print(stack[-1] if stack else -1, end=' ')
	stack.append(num)