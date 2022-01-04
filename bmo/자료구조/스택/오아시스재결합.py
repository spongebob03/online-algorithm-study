f = open("input.txt", "r")

n = int(f.readline())

p = [int(f.readline()) for _ in range(n)]
answer = n -1 # 기본적으로 이웃끼리 볼 수 있으므로

for i in range(n):
    for j in range(n-1, i+1, -1):
        # print(p[i], p[j], p[i+1:j])
        middle = max(p[i+1:j])
        if middle > p[i] or middle > p[j]:
            continue
        answer += 1

print(answer)