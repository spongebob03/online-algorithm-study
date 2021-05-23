from collections import deque 

def solution(jobs):
    # 각 작업의 요청부터 종료까지 걸린 시간의 합 
    answer = 0
    # 작업의 개수 
    N = len(jobs)
    
    # 요청 시점이 이른 순대로, 요청 시점이 같다면 소요 시간이 적은 순대로 정렬
    jobs.sort(key=lambda x: (x[0], x[1]))
    
    # 현재: 첫 작업의 요청 시점 
    now = jobs[0][0]
    
    jobs = deque(jobs)
    
    while jobs:
        request, elapsedTime = jobs.popleft()
        
        # 요청 시점이 이미 지난 경우 
        if now > request:
            # 바로 작업 시작해서 소요시간만큼 시간이 더 흐름 
            now += elapsedTime 
            # 요청 시점이 지나서 작업을 시작했으므로, 요청부터 종료까지 걸린 시간은 (해당 작업이 끝난 현재 시점) - (요청 시점) 
            answer += now - request
        # 아직 요청 시점이 오지 않은 경우 
        else:
            # 요청 시점부터 해당 작업 시작하기 
            now = request + elapsedTime 
            # 요청 하자마자 작업을 했으므로, 요청부터 종료까지 걸린 시간은 작업의 소요시간과 같음 
            answer += elapsedTime
        
        # 해당 작업을 수행하고 있는데 새로운 작업이 요청 들어온 경우 
        waitingList = []
        for job in jobs:
            if job[0] < now:
                waitingList.append(job)
            else:
                break
        
        # 새로 요청 들어온 작업들을 jobs에서 없애고 
        for w in waitingList:
            jobs.remove(w)
            
        # 소요시간 짧은 순대로 정렬 
        waitingList.sort(key=lambda x: x[1])
        
        # 소요시간 짧은 순대로 정렬한 새로 요청 들어온 작업을 jobs와 다시 합침 
        jobs = deque(waitingList) + jobs
                
    
    return int(answer / N)