from collections import deque

t = int(input())

res = []
for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(k):
        x, y = map(int, input().split())
        # y를 짓기 위해서는 x를 지어야 한다.
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    
    # 진입차수가 0인 노드들
    q = deque()
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] += d[i]

    while q:
        x = q.popleft()
        for y in graph[x]:
            indegree[y] -= 1
            dp[y] = max(dp[y], dp[x] + d[y])
            if indegree[y] == 0:
                q.append(y)
    res.append(dp[w])

print(*res, sep='\n')