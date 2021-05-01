n, m = map(int, input().split())
lst = list(map(int, input().split()))

n_lst = lst.pop(0)
parent = [i for i in range(n+1)]
for i in range(n_lst):
    parent[lst[i]] = -1

def find_parent(x, parent):
    if parent[x] == -1:
        return -1
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

party = [[]]
for _ in range(m):
    tmp = list(map(int, input().split()))
    n_tmp = tmp.pop(0)
    for i in range(n_tmp):
        for j in range(n_tmp):
            if find_parent(tmp[i], parent) != find_parent(tmp[j], parent):
                union(tmp[i], tmp[j], parent)
    party.append(tmp)

answer = 0
for i in range(1, m+1):
    if not party[i]:
        answer += 1
        continue
    if find_parent(party[i][0], parent) != -1:
        answer += 1

print(answer)