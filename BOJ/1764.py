n, m = map(int, input().split())
no_listen = set()
no_see = set()

for _ in range(n):
    no_listen.add(input())

for _ in range(m):
    no_see.add(input())

both = sorted(no_listen & no_see)
print(len(both))
print(*both, sep='\n')