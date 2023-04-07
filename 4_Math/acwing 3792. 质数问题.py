def func(n, k):
	primes, is_prime = [], [1 for _ in range(n + 1)]
	for i in range(2, n + 1):
		if is_prime[i]: primes.append(i)
		for j in range(len(primes)):
			c = primes[j] * i
			if c > n: break
			is_prime[c] = 0
			if i % primes[j] == 0: break
	d, cnt = set(primes), 0
	for i in range(1, len(primes)):
		if (primes[i - 1] + primes[i] + 1) in d: cnt += 1
	return cnt >= k


for _ in range(int(input())):
	n, k = map(int, input().split())
	print('YES' if func(n, k) else 'NO')