n = int(input())
se = ' ' + input()
set_ = set()

for l in range(1, 101):
	for i in range(1, n - l + 1 + 1):
		if se[i: i + l] in set_: break
		else:
			if i == n - l + 1:
				print(l)
				exit()
			set_.add(se[i: i + l])
