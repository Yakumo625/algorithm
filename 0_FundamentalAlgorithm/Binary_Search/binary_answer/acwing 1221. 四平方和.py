from math import sqrt

n = int(input())
dict_ = dict()

for c in range(int(sqrt(n)) + 1):
	if c*c > n: break
	for d in range(int(sqrt(n)) + 1):
		if c*c + d*d > n: break
		if (c*c + d*d) in dict_: continue
		dict_[c*c + d*d] = (c, d)

for a in range(int(sqrt(n)) + 1):
	if a*a > n: break
	for b in range(int(sqrt(n)) + 1):
		if a*a + b*b > n: break
		if (n - a*a - b*b) in dict_:
			print(a, b, *dict_[n - a*a - b*b])
			exit()