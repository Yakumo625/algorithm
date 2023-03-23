# p, q = 0, 1
# for _ in range(int(input())):
# 	print(p, end=' ')
# 	p, q = q, p + q

# print(*(lambda n: (fib := lambda x: x-1 if x <= 2 else fib(x-1) + fib(x - 2), [fib(i) for i in range(1, n+1)])) (int(input()))[1])

from collections import defaultdict as ddict

mem = ddict(int)

def fib(n):
	if n <= 2: return n - 1
	if mem[n]: return mem[n]
	mem[n] = fib(n - 1) + fib(n - 2)
	return mem[n]

print(*[fib(n) for n in range(1, int(input()) + 1)])