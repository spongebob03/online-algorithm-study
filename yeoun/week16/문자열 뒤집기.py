import sys

s = sys.stdin.readline()

# s에서 연속된 중복을 없앤 string
x = s[0]
for i in range(len(s)):
    if i == 0 or s[i] == x[-1]:
        continue
    else:
        x += s[i]

# 불연속인 0의 개수와 불연속인 1의 개수 중 최솟값
print(min(x.count('0'), x.count('1')))
