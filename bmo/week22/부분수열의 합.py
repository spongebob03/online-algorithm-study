import itertools

n, s = 5, 0
nums = list(map(int, "-7 -3 -2 5 8".split()))

answer = 0
if sum(nums) == s:
    answer += 1

for cnt in range(1, n):
    for combi in itertools.combinations(nums, cnt):
        if sum(combi) == s:
            answer += 1

print(answer)