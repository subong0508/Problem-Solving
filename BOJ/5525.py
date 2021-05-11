import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

i = 0
answer = 0
while i < m:
    if s[i] == 'O':
        i += 1
    else:
        cnt = 1
        now = s[i]
        j = i + 1
        while j < m:
            if now != s[j]:
                cnt += 1
                now = s[j]
                j += 1
            else:
                if now == 'O':
                    cnt -= 1
                    j += 1
                break
        if cnt >= 2*n+1:
            answer += (cnt - (2*n+1)) // 2 + 1
        i = j

print(answer)