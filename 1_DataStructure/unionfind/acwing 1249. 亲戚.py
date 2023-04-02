import sys

input = lambda :sys.stdin.readline()
print = lambda x : sys.stdout.write(x + '\n')

n, m = map(int, input().split())
fa = [i for i in range(n + 1)]

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

def merge(x, y):
    a, b = find(x), find(y)
    fa[a] = b

for _ in range(m):
    x, y = map(int, input().split())
    merge(x, y)

for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if find(x) == find(y) else 'No')
