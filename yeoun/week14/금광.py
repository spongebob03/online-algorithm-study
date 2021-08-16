import fileinput

# 입력 처리하기
for i, line in enumerate(fileinput.input()):
    if i == 0:
        # 테스트 케이스 개수
        N = int(line)
        tests = []
        sizes = []
    elif i % 2 == 1:
        # 금광 크기
        a, b = list(map(int, line.split()))
        sizes.append((a,b))
        tests.append([[0]*b for _ in range(a)])
    else:
        a, b = len(tests[-1]), len(tests[-1][0])
        vals = list(map(int, line.split()))
        for row, i in enumerate(range(0, len(vals), b)):
            tests[-1][row] = vals[i:i+4]


for test, size in zip(tests, sizes):
    a, b = size
    # 1열, 2열, ... b열까지 
    for j in range(b):
        for i in range(a):
            # 첫 열
            if j == 0:
                continue
            # 첫 행 (왼쪽, 왼쪽 아래에서 접근 가능)
            elif i == 0:
                test[i][j] += max(test[i][j-1], test[i+1][j-1])
            # 마지막 행 (왼쪽 위, 왼쪽에서 접근 가능)
            elif i == (a-1):
                test[i][j] += max(test[i-1][j-1], test[i][j-1])
            # 중간 행 (왼쪽 위, 왼쪽, 왼쪽 아래에서 접근 가능)
            else:
                test[i][j] += max(test[i-1][j-1], test[i][j-1], test[i+1][j-1])

    # 마지막 열의 값들 중 최댓값
    print(max([row[-1] for row in test]))