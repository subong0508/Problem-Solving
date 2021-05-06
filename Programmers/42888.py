def solution(record):
    answer = []
    members = {}
    for r in record:
        lst = r.split()
        msg = lst[0]
        user = lst[1]
        if msg == "Enter":
            members[user] = lst[2]
            answer.append((user, "Enter"))
        elif msg == "Leave":
            answer.append((user, "Leave"))
        elif msg == "Change":
            members[user] = lst[2]
    for i, (user, msg) in enumerate(answer):
        if msg == "Enter":
            answer[i] = members[user] + "님이 들어왔습니다."
        elif msg == "Leave":
            answer[i] = members[user] + "님이 나갔습니다."
    return answer