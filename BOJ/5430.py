import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    tmp = input().rstrip()[1:-1].split(',')
    arr = []
    for i in range(n):
        arr.append(tmp[i])
    arr_r = arr[::-1]
    arr = deque(arr)
    arr_r = deque(arr_r)
    error = False
    for ch in p:
        if ch == 'R':
            arr, arr_r = arr_r, arr
        elif not arr:
            error = True
            break
        else:
            arr.popleft()
            arr_r.pop()
    if error:
        res.append('error')
    else:
        res.append('[' + ','.join(arr) + ']')

print(*res, sep='\n')