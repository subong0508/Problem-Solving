t = int(input())

def calc_comb(n):
    clothes = {}
    for _ in range(n):
        v, k = input().split()
        if k not in clothes:
            clothes[k] = [v]
        else:
            clothes[k].append(v)
    answer = 1
    for k, v in clothes.items():
        answer *= len(v) + 1
    answer -= 1
    return answer

res = []
for _ in range(t):
    n = int(input())
    res.append(calc_comb(n))

print(*res, sep='\n')