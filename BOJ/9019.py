from collections import deque

def bfs(start, end):
    q = deque([(start, '')])
    visited = [False] * 10000
    visited[start] = True
    while q:
        now, string = q.popleft()
        if now == end:
            return string
        tmp = (2*now) % 10000
        if not visited[tmp]:
            visited[tmp] = True
            q.append((tmp, string + 'D'))
        tmp = now-1 if now != 0 else 9999
        if not visited[tmp]:
            visited[tmp] = True
            q.append((tmp, string + 'S'))
        tmp = str(now)
        if len(tmp) < 4:
            tmp = '0' * (4-len(tmp)) + tmp
        left = int(tmp[-3:] + tmp[0])
        if not visited[left]:
            visited[left] = True
            q.append((left, string + 'L'))
        right = int(tmp[-1] + tmp[:3])
        if not visited[right]:
            visited[right] = True
            q.append((right, string  + 'R'))

t = int(input())
res = []
for _ in range(t):
    a, b = map(int, input().split())
    res.append(bfs(a, b))

print(*res, sep='\n')