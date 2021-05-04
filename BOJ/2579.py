n = int(input())
stairs = []
for _  in range(n):
    stairs.append(int(input()))

# 연속, 불연속
dp = [[0, 0] for _ in range(n)]
for i in range(n-1, -1, -1):
    if i == n-1:
        dp[i][0] = dp[i][1] = stairs[i]
    else:
        if 0 <= i+1 < n:
            dp[i][0] = dp[i+1][1] + stairs[i]
        if 0 <= i+2 < n:
            dp[i][1] = max(dp[i+2]) + stairs[i]

if n >= 2:
    print(max(max(dp[0]), max(dp[1])))
else:
    print(stairs[0])