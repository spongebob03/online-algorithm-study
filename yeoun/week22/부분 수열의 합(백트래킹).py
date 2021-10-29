import sys

N,S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

count = 0

def backtracking(sum,idx):
	# global keyword allows you to modify the variable outside of the current scope
	global count
	if idx >= N:
		return
	sum += nums[idx]
	if sum == S:
		count += 1 
	# 현재 숫자를 포함하는 경우 
	backtracking(sum, idx+1)
	# 현재 숫자를 포함하지 않는 경우 
	backtracking(sum-nums[idx], idx+1)

backtracking(0,0)
print(count)