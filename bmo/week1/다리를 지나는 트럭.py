from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = deque(truck_weights)
    ongoing = deque()

    while queue:
        time += 1
        
        for truck in list(ongoing):
            if truck[1] > time:
                break
            ongoing.popleft()

        if not ongoing or sum([weight for weight, time in ongoing]) + queue[0] <= weight:
            ongoing.append((queue.popleft(),time + bridge_length))

    time = ongoing[-1][-1]
    return time