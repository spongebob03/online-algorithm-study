n = int(input())

houses = list(map(int, input().split()))
houses.sort()

answer = houses[n // 2 - 1] if n % 2 == 0 else houses[n // 2]

print(answer)