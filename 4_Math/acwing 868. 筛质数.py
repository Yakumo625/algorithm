def func(n):
    res = 0
    primes, is_prime = [], [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        if is_prime[i]:
            res += 1
            primes.append(i)
        for j in range(len(primes)):
            c = primes[j] * i
            if c > n: break
            is_prime[c] = 0
            if i % primes[j] == 0: break
    return set([prime for prime in primes if prime & 1])

print(func(int(input())))