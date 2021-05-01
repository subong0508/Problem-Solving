from collections import deque

n, k = map(int, input().split())

q = deque([(n, 0)])
visited = [False] * (100001)
visited[n] = True
while q:
    now, cnt = q.popleft()
    if now == k:
        print(cnt)
        break
    if 0 <= now-1 < len(visited) and not visited[now-1]:
        visited[now-1] = True
        q.append((now-1, cnt+1))
    if 0 <= now+1 < len(visited) and not visited[now+1]:
        visited[now+1] = True
        q.append((now+1, cnt+1))
    if 0 <= 2*now < len(visited) and not visited[2*now]:
        visited[2*now] = True
        q.append((2*now, cnt+1))
