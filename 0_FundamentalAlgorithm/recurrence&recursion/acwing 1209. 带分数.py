# from itertools import permutations as pmtts

# n = int(input())
# pmtt = pmtts(range(1, 10))

# ans = 0
# for p in pmtt:
# 	a = 0
# 	for l in range(len(str(n))):

# 		a = a * 10 + p[l]
# 		if a >= n: break

# 		for r in range((l+9) >> 1, 8):
# 			b = c = 0

# 			for w in range(l+1, r+1):
# 				b = b * 10 + p[w]
# 			for v in range(r+1, 9):
# 				c = c * 10 + p[v]

# 			if b % c  == 0 and a + b // c == n:
# 				ans += 1

# print(ans)


from itertools import *

N = int(input())


p = permutations(range(1, 10))

res = 0
for i in p:
    l = ''.join(map(str, i))
    for p1 in range(len(str(N))):
        for p2 in range((p1+9)//2, 9):
            if int(l[:p1+1]) + int(l[p1+1:p2]) / int(l[p2:]) == N:
                res += 1

print(res)