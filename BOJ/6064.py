import sys

input = sys.stdin.readline
t = int(input())
res = []
for _ in range(t):
    m, n, x, y = map(int, input().split())
    found = False
    for i in range(x, m*n+1, m):
        a = i % m 
        b = i % n
        a = m if a == 0 else a
        b = n if b == 0 else b
        if a == x and b == y:
            res.append(i)
            break
    else:
        res.append(-1)

print(*res, sep='\n')