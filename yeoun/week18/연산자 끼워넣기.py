import sys
from itertools import permutations

# 수의 개수
N = int(sys.stdin.readline())
# 주어진 수들
nums = list(map(int, sys.stdin.readline().split()))
# 연산자
operator_list = list(map(int, sys.stdin.readline().split()))
operators = []
for i, op in enumerate(operator_list):
    if i == 0:
        operators += ['+'] * op
    elif i == 1:
        operators += ['-'] * op
    elif i == 2:
        operators += ['*'] * op
    else:
        operators += ['//'] * op

# permutations은 같은 기호 2개 이상 있을 때 둘을 다른 것으로 구분하므로, set을 통해 중복을 제거해줘야 함 
permuted_operators = list(set(permutations(operators)))

# 연산자 permutation에 따른 모든 값들의 리스트 
vals = []

for op in permuted_operators:
    val = nums[0]
    for num, o in zip(nums[1:], op):
        if o == '+':
            val += num
        elif o == '-':
            val -= num
        elif o == '*':
            val *= num
        else:
            if val < 0:
                val = (-1) * (((-1) * val) // num)
            else:
                val //= num
    vals.append(val)

print(max(vals)) # 최댓값
print(min(vals)) # 최솟값
