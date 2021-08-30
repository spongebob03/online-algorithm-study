f = open('bmo/week17/input2.txt')
n = int(f.readline())
k = int(f.readline())

board = [[0] * (n) for _ in range(n)]
dummy = ((0, 0), 1, 0) # 머리위치 (x, y), 몸길이, 각도

for _ in range(k):
    x, y = map(int, f.readline().split())
    board[x-1][y-1] = 1

changes = {}
l = int(f.readline())
for _ in range(l):
    t, d = f.readline().split()
    changes[int(t)] = d

time = 0

while True:
    if time in changes.keys():
        if changes[time] == 'D':
            dummy[2] += 90
        else:
            dummy[2] += -90
    time += 1
    
# 보드 안에서 움직이는건지 판별