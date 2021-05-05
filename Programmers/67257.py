from itertools import permutations

def parse(expression):
    num = ''
    exp = []
    for e in expression:
        if e.isdigit():
            num += e
        else:
            exp.append(int(num))
            num = ''
            exp.append(e)
    exp.append(int(num))
    return exp

def infix_to_postfix(expression, priorities):
    stack = []
    res = []
    for e in expression:
        if type(e) == int:
            res.append(e)
        else:
            while stack and priorities[e] >= priorities[stack[-1]]:
                res.append(stack.pop())
            stack.append(e)
    while stack:
        res.append(stack.pop())
    return res

def calc_postfix(expression):
    stack = []
    for e in expression:
        if type(e) == int:
            stack.append(e)
        else:
            if e == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1+num2)
            elif e == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1-num2)
            elif e == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1*num2)
    return stack.pop()

def solution(expression):
    answer = 0
    expression = parse(expression)
    ops = set(e for e in expression if type(e) == str)
    combs = permutations(ops, len(ops))
    for comb in combs:
        priorities = {}
        cnt = 0
        for c in comb:
            priorities[c] = cnt
            cnt += 1
        postfix = infix_to_postfix(expression, priorities)
        answer = max(answer, abs(calc_postfix(postfix)))
    return answer