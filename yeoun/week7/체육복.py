def solution(n, lost, reserve):
    # 빌려주기 전 체육 수업을 들을 수 있는 학생의 수 
    answer = n - len(lost)
    
    # 모두 오름차순으로 정렬
    lost.sort()
    reserve.sort()
    
    # 여벌의 체육복이 있고, 도난도 당한 학생 
    self_lend = set(lost) & set(reserve)
    # 자신의 여벌의 체육복을 입으면 되므로 이런 학생 수만큼 answer 증가 
    answer += len(self_lend)
    # 이미 계산했으므로 lost, reserve 리스트에 이런 학생 삭제 
    for sl in self_lend:
        lost.remove(sl)
        reserve.remove(sl)
    
    # 도난당한 학생들 중에서 
    for lo in lost:
        # 먼저 앞번호 학생한테 빌리기 시도 
        # 그래야 그 다음 도난당한 학생들이 뒷번호 학생한테 빌릴 수 있는 가능성 있어 최대한 많은 학생이 체육 수업을 들을 수 있음 
        if (lo-1) in reserve:
            reserve.remove(lo-1)
            answer += 1 
        # 앞번호 학생에게 빌릴 수 없으면 뒷번호 학생에게 빌릭 
        elif (lo+1) in reserve:
            reserve.remove(lo+1)
            answer += 1 

    return answer