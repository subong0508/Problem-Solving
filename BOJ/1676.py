n = int(input())

fact = 1
for i in range(1, n+1):
    fact *= i

fact = str(fact)
i = len(fact)-1
answer = 0
while i >= 0:
    if fact[i] != '0':
        break
    answer += 1
    i -= 1

print(answer)