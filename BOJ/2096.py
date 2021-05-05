import sys

input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    a, b, c = map(int, input().split())
    dp.append([a, b, c])

dp_min = dp[0][:]
dp_max = dp[0][:]

for i in range(1, n):
    dp_min_ = dp[i][:]
    dp_max_ = dp[i][:]
    for j in range(3):
        if j == 0:
            dp_min_[j] += min(dp_min[j], dp_min[j+1])
            dp_max_[j] += max(dp_max[j], dp_max[j+1])
        elif j == 1:
            dp_min_[j] += min(dp_min)
            dp_max_[j] += max(dp_max)
        else:
            dp_min_[j] += min(dp_min[j-1], dp_min[j])
            dp_max_[j] += max(dp_max[j-1], dp_max[j])
    dp_min = dp_min_
    dp_max = dp_max_

print(max(dp_max), min(dp_min))