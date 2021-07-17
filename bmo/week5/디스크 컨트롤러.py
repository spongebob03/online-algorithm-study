def solution(jobs):
    answer = 0
    time = 0

    # 요청 빨리 끝나는 것부터 처리
    jobs.sort(key=lambda x: (x[1], x[0]))
    for call, end in jobs:
        time += end
        answer += time - call

    return answer // len(jobs)