import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

query = []
for _ in range(m):
    a, b = map(int, input().split())
    query.append((a, b))

for i in range(1, n+1):
    arr[i] += arr[i-1]

res = []
for a, b in query:
    res.append(arr[b] - arr[a-1])

print(*res, sep='\n')