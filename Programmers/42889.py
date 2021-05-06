def solution(N, stages):
    answer = []
    prev = 0
    stages.sort()
    # 클리어하지 못한 플레이어의 수, 스테이지에 도달한 플레이어 수
    d = {i: [0, 0] for i in range(1, N+1)}
    prev = stages[0]
    total = len(stages)
    cnt = 1
    for i in range(1, len(stages)):
        if stages[i] != prev:
            d[prev] = [cnt, total]
            prev = stages[i]
            total -= cnt
            cnt = 1
        else:
            cnt += 1
    if prev in d:
        d[prev] = [cnt, total]
    for k in d:
        if d[k][1] == 0:
            d[k] = 0
        else:
            d[k] = d[k][0] / d[k][1]
    answer = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in answer]
    return answer