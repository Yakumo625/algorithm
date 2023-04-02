from collections import defaultdict as ddict

a, b = input(), input()
d = ddict(int)

for i in range(len(a)):
    c = str(int(a[i]) ^ 1)
    res = a[:i] + c + a[i + 1:]
    d[int(res ,2)] += 1

seq = ('0', '1', '2')
for i in range(len(b)):
    for c in seq:
        if b[i] != c:
            res = b[:i] + c + b[i + 1:]
            d[int(res, 3)] += 1

for k, v in d.items():
    if v > 1:
        res, kk = '', k
        while kk > 1:
            res += str(kk % 2)
            kk //= 2
        if len(res) + 1 != len(a): continue
        else:
            print(k)
    
