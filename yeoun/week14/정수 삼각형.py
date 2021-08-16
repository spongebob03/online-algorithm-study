import sys

# 입력 처리하기
nums = []
# 삼각형의 크기
N = int(sys.stdin.readline())
for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))

for i, num in enumerate(nums):
    # 첫 행
    if i == 0 :
        continue
    for j in range(i+1):
        # i행의 첫 번째 숫자: 직전 행의 첫 번째 숫자에서만 접근 가능
        if j == 0:
            nums[i][j] += nums[i-1][j]
        # i행의 마지막 숫자: 직전 행의 마지막 숫자에서만 접근 가능
        elif j == i:
            nums[i][j] += nums[i - 1][j-1]
        # 직전 행의 왼쪽, 오른쪽 대각선에서 모두 접근 가능
        else:
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])

# 마지막 행의 최댓값 
print(max(nums[-1]))