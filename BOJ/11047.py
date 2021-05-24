import sys

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
coins = []
for _ in range(n):
    a = int(input())
    coins.append(a)
coins.reverse()

answer = 0
for i in range(n):
    tmp = k // coins[i]
    answer += tmp
    k -= tmp * coins[i]
    if k == 0:
        break

print(answer)