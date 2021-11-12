# 프로그래머스 위클리챌린지 문제
def solution(scores):
    answer = ''
    n = len(scores)
    
    for i in range(n):
        subjects = []
        for score in scores:
            subjects.append(score[i])
        
        max_score = max(subjects)
        min_score = min(subjects)
        average = sum(subjects) / len(subjects)
        if score[i] in (max_score, min_score) and subjects.count(score[i]):
            average = (sum(subjects[:i]) + sum(subjects[i+1:])) / (len(subjects) - 1)
            
        if average >= 90:
            answer += 'A'
        elif 80 <= average < 90:
            answer += 'B'
        elif 70 <= average < 80:
            answer += 'C'
        elif 50 <= average < 70:
            answer += 'D'
        else:
            answer += 'F'

    return answer

scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores))