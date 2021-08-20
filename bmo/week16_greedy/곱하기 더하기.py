n = '567'

answer = 0

for num in n:
    if answer == 0 or num in ('0', '1'):
        answer += int(num)
    else:
        answer *= int(num)

print(answer)