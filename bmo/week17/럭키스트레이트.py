n = input()
m = len(n) // 2

answer = "LUCKY" if sum(map(int,n[:m])) == sum(map(int, n[m:])) else "READY"
print(answer)