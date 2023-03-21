# p, q = 0, 1
# for _ in range(int(input())):
# 	print(p, end=' ')
# 	p, q = q, p + q

(lambda n=int(input()): reduce(lambda x, _: x + [x[-2] + x[-1]], range(n-2), [0, 1][:n]))()