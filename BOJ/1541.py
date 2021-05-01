formula = input()
answer = 0
lst = formula.split('-')

for i, l in enumerate(lst):
    tmp = [int(x) for x in l.split('+')]
    if i == 0:
        answer += sum(tmp)
    else:
        answer -= sum(tmp)

print(answer)