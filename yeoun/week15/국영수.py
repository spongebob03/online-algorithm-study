import sys

# 학생 수
N = int(sys.stdin.readline())

students = []
for i in range(N):
    # 이름, 국어, 영어, 수학
    name, korean, english, math = list(sys.stdin.readline().split())
    students.append((name, int(korean), int(english), int(math)))

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in students:
    print(student[0])
