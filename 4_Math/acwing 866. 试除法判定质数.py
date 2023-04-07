n = int(input())

def is_prime(a):
	for i in range(2, a):
		if i * i > a: break
		if a % i == 0: return 0
	return 0 if a == 1 else 1

for _ in range(n):
	if is_prime(int(input())): print('Yes')
	else: print('No')