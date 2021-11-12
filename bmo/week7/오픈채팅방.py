def solution(record):
    answer = []
    users = dict()
    COMMAND, UID, NICK = 0, 1, 2
    
    for log in record:
        log = log.split()
        if log[COMMAND] == 'Enter':
            users[log[UID]] = log[NICK]
        elif log[COMMAND] == 'Change':
            users[log[UID]] = log[NICK]
    
    for log in record:
        log = log.split()
        if log[COMMAND] == 'Enter':
            log[COMMAND] = '들어왔습니다'
        elif log[COMMAND] == 'Leave':
            log[COMMAND] == '나갔습니다'
        else:
            continue
        answer.append(f'{users[log[UID]]}님이 {log[COMMAND]}')
    return answer

if __name__ == '__main__':
    solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])