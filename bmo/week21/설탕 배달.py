n = int(input())

answer = n # 만들 수 있는 최대 봉지 수는 n 이하일 것

bag5 = n // 5
for i in range(bag5 + 1):
    sugar = n - (5 * i)
    if sugar % 3 == 0:
        answer = min(answer, i + (sugar // 3))

print(answer) if answer != n else print(-1)