import sys
N = int(sys.stdin.readline())
scores = []
for _ in range(N):
	scores.append(int(sys.stdin.readline()))

scores.reverse()

answer = 0
i = 0
consecutive = 0 
while i < len(scores):
	if i == 0:
		answer += scores[0]
		i += 1 
		consecutive += 1 
	elif:
		if consecutive < 3 and scores[i] >= scores[i+1]:
			answer += scores[i]
			i += 1 
			consecutive += 1 
		else:
			answer += scores[i+1]
			i += 2 
			consecutive = 0 

print(answer)

