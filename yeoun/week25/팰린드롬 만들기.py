# 틀렸습니다
# 참고: https://js1jj2sk3.tistory.com/45
import sys
import copy
from collections import deque


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 앞뒤가 같은 쌍의 개수
def palindrome_count(nums):
	substring = deque(copy.deepcopy(nums))
	count = 0
	while len(substring) > 1 and substring[0] == substring[-1]:
		substring.pop()
		substring.popleft()
		count += 1
	return count

def add_num(nums):
	# 0번째 숫자를 맨 뒤에 추가하는 경우와 마지막 숫자를 맨 앞에 추가하는 경우 비교
	# 0번째 숫자를 맨 뒤에 추가
	if palindrome_count(nums[1:]) > palindrome_count(nums[:-1]):
		return nums[1:]
	# 마지막 숫자를 맨 앞에 추가
	else:
		return nums[:-1]

answer = 0
while len(nums) > 1:
	# 앞뒤 쌍이 같으면 숫자 추가하지 않고 넘어감
	if nums[0] == nums[-1]:
		nums = nums[1:-1]
		continue
	# 앞 또는 뒤에 숫자 추가
	nums = add_num(nums)
	answer += 1

print(answer)

