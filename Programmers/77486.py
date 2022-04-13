# 77486. 다단계 칫솔 판매


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    # 이름을 key, 인덱스를 value로 갖는 딕셔너리 생성
    relation = dict()
    for index, person in enumerate(enroll):
        relation[person] = index

    for index, person in enumerate(seller):
        person = relation[person]  # 현재 사람의 인덱스
        money = amount[index] * 100  # 현재 번 돈
        while 1 <= money:  # 10%를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않음
            answer[person] += money - int(money * 0.1)  # 본인 몫
            if referral[person] == "-":  # 피라미드 정상에 도달한 경우 탐색 종료
                break
            person = relation[referral[person]]  # 추천인
            money = int(money * 0.1)  # 추천인에게 전달될 돈

    return answer
