from collections import defaultdict

def solution(n, lost, reserve):
    student = defaultdict(int)

    for i in range(1, n+1):
        student[i] += 1
    for l in lost:
        student[l] -= 1
    for r in reserve:
        student[r] += 1
    
    for i in range(n, 1, -1):
        if student[i] == 2 and student[i-1] == 0:
            student[i] -= 1
            student[i-1] += 1

    for i in range(1, n):
        if student[i] == 2 and student[i+1] == 0:
            student[i] -= 1
            student[i+1] += 1

    for value in student.values():
        if value == 0:
            n -= 1

    return n