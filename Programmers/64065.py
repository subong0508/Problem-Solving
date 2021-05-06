def solution(s):
    answer = []
    s = s[1:-1][1:-1]
    s = s.split('},{')
    total = []
    for x in s:
        tmp = x.split(',')
        total.append(list(map(int, tmp)))
    total.sort(key=lambda x: len(x))
    s = set()
    for subset in total:
        for t in subset:
            if t not in s:
                answer.append(t)
                s.add(t)
    return answer