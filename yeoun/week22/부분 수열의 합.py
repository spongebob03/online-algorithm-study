import sys
from itertools import combinations

N,S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(1,N+1):
	combs = list(combinations(nums,i))
	for comb in combs:
		if sum(comb) == S:
			answer += 1
print(answer)
