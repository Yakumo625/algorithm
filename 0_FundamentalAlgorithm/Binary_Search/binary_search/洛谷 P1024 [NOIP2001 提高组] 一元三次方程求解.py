a, b, c, d = map(float, input().split())

func = lambda x : a * x ** 3 + b * x ** 2 + c * x + d

cnt = 0

for i in range(-100, 100):

	if cnt == 3: break

	if func(i) == 0:
		print('%.2lf'%i, end=' ')
		cnt += 1

	l, r = i, i + 1

	if func(l) * func(r) < 0:
		while r - l > 1e-4:
			mid = (l + r) / 2
			if func(mid) * func(r) >= 0: r = mid
			else: l  = mid
		print('%.2lf'%r, end=' ')
		cnt += 1

if func(100) == 0:
	print('100.00')


