import sys
import math

def stars(k):
	if k == 1:
		return ['***','* *', '***']
	else:
		result = []
		prev_stars = stars(k-1)
		# 이전 모양 3개 위에 쌓기 
		for row in prev_stars:
			result.append(row * 3)
		# 이전 모양 + (N/3 * N/3) 크기의 빈 사각형 + 이전 모양 
		for row in prev_stars:
			result.append(row + ' ' * int(3**(k-1)) + row)
		# 이전 모양 3개 아래에 쌓기
		for row in prev_stars:
			result.append(row * 3)
		return result

N = int(sys.stdin.readline())
# N = 81일 때 4.0, N = 243일 때 4.999 라서 int 아니고 round 해줘야 함 
k = round(math.log(N, 3))

for s in stars(k):
	print(s)