f = open("input.txt", "r")

n = int(f.readline())

HEIGHT, CNT = 0, 1 # (키, 이 사람이 볼 수 있는 사람)

answer = 0
stack = []

for _ in range(n):
    curr = int(f.readline())

    while stack and stack[-1][HEIGHT] < curr:
        # 스택에 들어있는 앞사람들보다 키가 더 큰 사람이 있으면
        # 앞사람들은 더 볼 수 없을거니까 pop
        answer += stack.pop()[CNT]

    if not stack:
        stack.append((curr, 1))
    else:
        if stack[-1][HEIGHT] == curr:
            cnt = stack.pop()[CNT]
            answer += cnt
            if stack:
                answer += 1
            stack.append((curr, cnt + 1))
        else:
            stack.append((curr, 1))
            answer += 1
            
    print(stack)
print(answer)