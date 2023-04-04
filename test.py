import sys
from heapq import *

input = lambda : sys.stdin.readline()
write = lambda x: sys.stdout.write(str(x) + '\n')

heap = []
n = int(input())
for _ in range(n):
    op, *x = map(int, input().split())
    if op == 1: heappush(heap, x[0])
    elif op == 2: print(heap[0])
    else: heappop(heap)



# import sys

# input = lambda : sys.stdin.readline()
# print = lambda x : sys.stdout.write(str(x) + '\n')

# def swap(x, y): heap[x], heap[y] = heap[y], heap[x]

# def up(i):
#     while i > 0 and heap[i] < heap[i >> 1]:
#         swap(i, i >> 1)
#         i >>= 1

# def down(i):
#     while i * 2 <= size:
#         son = i * 2
#         if son < size and heap[son + 1] < heap[son]: son += 1
#         if heap[son] < heap[i]:
#             swap(son, i)
#             i = son
#         else: break

# n = int(input())
# heap, size = [0] * (n + 1), 0

# for _ in range(n):
#     op, *x = map(int, input().split())
#     if op == 1:
#         size += 1
#         heap[size] = x[0]
#         up(size)
#     elif op == 2:
#         print(heap[1])
#     else:
#         heap[1] = heap[size]
#         size -= 1
#         down(1)