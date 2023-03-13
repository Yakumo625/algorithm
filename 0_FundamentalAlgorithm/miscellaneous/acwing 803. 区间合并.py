n = int(input())
intervals = sorted([tuple(map(int, input().split())) for _ in range(n)])

cnt = 1
l, r = intervals[0]

for ll, rr in intervals[1:]:
	if ll <= r: r = max(r, rr)
	else:
		l, r = ll, rr
		cnt += 1
	
print(cnt)
