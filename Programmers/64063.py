import sys

sys.setrecursionlimit(10 ** 6)

def find(r):
    if r not in rooms:
        rooms[r] = r+1
        return r
    else:
        x = find(rooms[r])
        rooms[r] = x
        return x

def solution(k, room_number):
    global rooms
    answer = []
    rooms = {}
    for r in room_number:
        answer.append(find(r))
    return answer