from collections import deque
import math

def solution(progresses, speeds):
    answer = [1]
    days = deque()

    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        days.append(day)

    prev_day = days.popleft()
    while days:
        curr = days.popleft()
        if curr <= prev_day:
            answer[-1] += 1
        else:
            answer.append(1)
            prev_day = curr
    return answer