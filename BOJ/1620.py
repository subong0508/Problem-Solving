n, m = map(int, input().split())
pockemon_to_int = {}
int_to_pockemon = {}

for i in range(1, n+1):
    pockemon = input()
    pockemon_to_int[pockemon] = i
    int_to_pockemon[i] = pockemon

res = []
for _ in range(m):
    x = input()
    if x.isdigit():
        res.append(int_to_pockemon[int(x)])
    else:
        res.append(pockemon_to_int[x])

print(*res, sep='\n')