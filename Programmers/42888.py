# 42888. 오픈채팅방


def solution(record):
    answer = []
    nicknames = {}  # 닉네임 기록 딕셔너리
    
    for r in record:
        command = r.split()
        
        # Enter, Change 명령의 경우 닉네임 갱신
        if 2 < len(command):
            nicknames[command[1]] = command[2]
            
        # Enter, Leave 명령의 경우 유저 아이디와 메시지 저장
        if command[0] == "Enter":
            answer.append([command[1], "님이 들어왔습니다."])
        elif command[0] == "Leave":
            answer.append([command[1], "님이 나갔습니다."])
    
    # 기록된 유저 아이디를 닉네임으로 변경
    for idx in range(len(answer)):
        answer[idx] = nicknames[answer[idx][0]] + answer[idx][1] 
    
    return answer