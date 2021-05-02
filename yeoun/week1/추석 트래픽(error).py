from collections import defaultdict
import datetime

def manageTime(line): # 요청 완료 시각, 소요시간을 입력으로 받음 
    _, end, time = line.split()
    h,m,s = end.split(':')
    s,ms = s.split('.')
    
    if '.' in time:
        ds, dms = time.split('.')
        dms = dms[:-1] # 끝부분 s 삭제
    else:
        ds = time[:-1]
        dms = 0 # 끝부분 s 삭제
    
    end = datetime.datetime(2016, 9, 15, int(h), int(m), int(s), int(ms)*1000)
    start = end - datetime.timedelta(seconds=int(ds), milliseconds=int(dms)) + datetime.timedelta(seconds=0, milliseconds=1)
    
    # 요청 시작 시각, 요청 완료 시각을 datetime으로 반환함 
    return start, end


def solution(lines):
    
    results = []
    # 요청 시작 시각이 key, 해당 요청의 lines 내의 index가 value인 dictionary 
    start_dict = defaultdict(lambda:[])
    # 요청 완료 시각이 key, 해당 요청의 lines 내의 index가 value인 dictionary 
    end_dict = defaultdict(lambda:[])
    
    # 모든 로그에 대해 시작 시각과 그 index를 start_dict, 완료 시각과 그 index를 end_dict에 저장 
    for i,line in enumerate(lines):
        s, e = manageTime(line)
        start_dict[s].append(i) # 같은 시각에 서로 다른 요청이 있을 수 있으므로 list에 append 하는 방식 사용 
        end_dict[e].append(i)
    
    # 모든 로그의 시작 시각, 완료 시각을 중복없이 모은 후 오름차순으로 정렬 
    sorted_log =  sorted(list(set(list(start_dict.keys()) + list(end_dict.keys()))))
    # 현재 시각 이전에 요청이 시작되었으며, 아직 완료되지 않은 것들의 lines 내 index 
    history = set()
    
    # 정렬된 로그 내 시각들을 하나씩 꺼내면서 
    for i, log in enumerate(sorted_log):
        # 현재 시각 
        current = log
        # 현재 시각 기준 1초동안 처리하는 요청들의 lines 내 index 
        current1sec = history.copy()
        
        # 현재 시각이 어떤 요청이 시작된 시각이라면 
        if current in start_dict:
            current1sec.update(start_dict[current])
        # 현재 시각이 어떤 요청이 완료된 시각이라면 
        if current in end_dict:
            current1sec.update(end_dict[current])
        
    
        next_idx = i+1
        
        # 다음 시각이 현재 시각 이후 1초 구간 내에 있다면 
        while next_idx < len(sorted_log) and sorted_log[next_idx] <= current + datetime.timedelta(seconds=1, milliseconds=0) - datetime.timedelta(seconds=0, milliseconds=1):
            
            # 다음 시각 
            next_log = sorted_log[next_idx]
            
            # 다음 시각이 어떤 요청이 시작된 시각이라면 
            if next_log in start_dict:
                current1sec.update(start_dict[next_log])
            # 다음 시각이 어떤 요청이 완료된 시각이라면 
            if next_log in end_dict:
                current1sec.update(end_dict[next_log])
            
            # while문을 처음으로 도는 상태라면 
            if next_idx == i+1:
                # 현재 current1sec를 history에 복사함 
                history = current1sec.copy()
                
                # 단, 다음 시각 이전에 끝난 요청들은 history에서 빼줘야 함 
                if current in end_dict:
                    history -= set(end_dict[current])
                if next_log in end_dict:
                    history -= set(end_dict[next_log])
            
            # sorted_log 내 다음 시각으로 
            next_idx += 1 
        
        # 각각의 현재 시각에 대해 처리한 요청들의 개수 
        results.append(len(current1sec))
            
        
    if results == []:
        return 1
    
    return max(results)
        
        