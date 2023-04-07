def func(x):
	res = []
	for i in range(1, x):
		if i * i > x: break
		if x % i == 0:
			res.append(i)
			if i * i != x: res.append(x // i)
	return sorted(res)

for _ in range(int(input())):
	print(*func(int(input())))
