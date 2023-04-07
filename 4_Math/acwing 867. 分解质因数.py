def func(a):
	for i in range(2, a):
		if i * i > a: break
		cnt = 0
		while a % i == 0:
			cnt += 1
			a //= i
		if cnt: print(i, cnt)
	if a > 1: print(a, 1)
	print()

for _ in range(int(input())):
	func(int(input()))