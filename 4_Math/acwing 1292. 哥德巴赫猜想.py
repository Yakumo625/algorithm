import sys

input = lambda : sys.stdin.readline()
print = lambda x : sys.stdout.write(x + '\n')

N = int(1e6)
primes, is_prime = [], [1 for _ in range(N + 1)]
for i in range(2, N + 1):
    if is_prime[i]:
        primes.append(i)
    for j in range(len(primes)):
        c = primes[j] * i
        if c > N: break
        is_prime[c] = 0
        if i % primes[j] == 0: break


while True:
	n = int(input())
	if not n: break
	for prime in primes:
	    if prime & 1 and (n - prime) & 1 and is_prime[prime] and is_prime[n - prime]:
	        print(f'{n} = {prime} + {n - prime}')
	        break