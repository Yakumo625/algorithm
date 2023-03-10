n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, m-1
s = 0

while s != x:
	s = a[i] + b[j]
	if s > x: j -= 1
	else: i += 1

print(i-1, j)

