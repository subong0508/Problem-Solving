import sys

input = sys.stdin.readline

n = int(input())
meeting = [(0, 0)] * n
for i in range(n):
    start, end = map(int, input().split())
    meeting[i] = start, end

meeting.sort(key=lambda x: (x[1], x[0]))
answer = 0
end = 0
for i in range(n):
    if meeting[i][0] >= end:
        answer += 1
        end = meeting[i][1]

print(answer)