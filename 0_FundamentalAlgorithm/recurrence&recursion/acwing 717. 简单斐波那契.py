# p, q = 0, 1
# for _ in range(int(input())):
# 	print(p, end=' ')
# 	p, q = q, p + q

print(*(lambda n: (fib := lambda x: x-1 if x <= 2 else fib(x-1) + fib(x - 2), [fib(i) for i in range(1, n+1)])) (int(input()))[1])