# 참고: https://it-garden.tistory.com/m/408?category=857251

import datetime

# string으로 주어진 로그를 datetime으로 변환 
def manageTime(line):
    _, end, time = line.split()
    h,m,s = end.split(':')
    s,ms = s.split('.')
    
    if '.' in time:
        ds, dms = time.split('.')
        dms = dms[:-1] # 끝부분 s 삭제
    else:
        ds = time[:-1]
        dms = 0 # 끝부분 s 삭제
    
    # 종료 시각
    end = datetime.datetime(2016, 9, 15, int(h), int(m), int(s), int(ms)*1000)
    # 시작 시각
    start = end - datetime.timedelta(seconds=int(ds), milliseconds=int(dms)) + datetime.timedelta(seconds=0, milliseconds=1)
    
    return start, end


def solution(lines):
    results = []
    
    # 각 요청의 처리 시작 시각과 종료 시각을 튜플로 저장한 리스트
    logs = []
    for line in lines:
        start, end = manageTime(line)
        logs.append((start, end))
    
    # 모든 요청에 대해
    for log in logs:
        # 각 요청의 처리 시작 시각과 종료 시각을 start로 가져옴 
        for start in log:
            # 1초 구간 내의 처리 개수를 알고 싶으므로 start 이후 1초가 지난 시각을 end로 설정
            end = start + datetime.timedelta(seconds=1)
            count = 0
            
            # start ~ end 구간에 포함되는 요청의 개수를 셈 
            for log in logs:
                # 특정 요청의 처리 종료 시각이 현재의 start 이후이고, 특정 요청의 처리 시작 시각이 현재의 end 이전이면 
                # (자기 자신은 항상 이 조건에 부합하므로 results의 최솟값은 1)
                if log[1] >= start and log[0] < end:
                    count += 1
            
            results.append(count)
    
    return max(results)