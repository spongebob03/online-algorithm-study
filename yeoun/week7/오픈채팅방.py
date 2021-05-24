def eng2ko(one_record, id2nickname):
    # 채팅방 들어오기
    if one_record.startswith('Enter'):
        user_id = one_record.split()[1]
        nickname = id2nickname[user_id]
        return nickname + '님이 들어왔습니다.'
        
    # 채팅방 나가기 
    elif one_record.startswith('Leave'):
        user_id = one_record.split()[1]
        nickname = id2nickname[user_id]
        return nickname + '님이 나갔습니다.'
        
    # 닉네임 변경 
    else:
        return 

def solution(record):
    answer = []
    
    # key: user id, value: 최신 닉네임 
    id2nickname = {}
    for rec in record:
        user_id = rec.split()[1]
        if len(rec.split()) > 2:
            nickname = rec.split()[2]
            # 가장 최근의 닉네임으로 계속 갱신
            id2nickname[user_id] = nickname
    
    for rec in record:
        result = eng2ko(rec, id2nickname)
        if result:
            answer.append(result)
    
    return answer