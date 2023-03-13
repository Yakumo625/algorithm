expre = input()

d = {'+': 1, '-': 1, '*': 2, '/': 2}
nums, ops = [], []

def cal():
	a, b, op = nums.pop(), nums.pop(), ops.pop()
	res = None
	if op == '+': res = b + a
	elif op == '-': res = b - a
	elif op == '*': res = b * a
	else: res = int(b / a)
	nums.append(res)

i = 0
while i < len(expre):
	if expre[i].isdigit():
		num = ''
		while i < len(expre) and expre[i].isdigit():
			num += expre[i]
			i += 1
		nums.append(int(num))
		i -= 1
	elif expre[i] == '(': ops.append('(')
	elif expre[i] == ')':
		while ops[-1] != '(': cal()
		ops.pop()
	else:
		while ops and ops[-1] != '(' and d[ops[-1]] >= d[expre[i]]: cal()
		ops.append(expre[i])
	i += 1

while ops: cal()
print(nums[-1])