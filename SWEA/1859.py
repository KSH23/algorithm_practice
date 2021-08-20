# 1859. 백만 장자 프로젝트


def millionaire(money):
    wallet = 0    # 벌어들인 돈
    date = 0    # 현재 날짜

    while date < len(money):
        price = money[date]  # 현재 최대 가격
        price_i = date  # 현재 최대 가격 인덱스

        # 현재 날짜 이후의 최대 가격을 구함
        for i in range(date, len(money)):
            if money[i] > price:
                price = money[i]
                price_i = i
        
        # 현재 날짜부터 최대 가격 날까지 모두 사고 모두 판다
        for j in range(date, price_i):
            wallet += price - money[j]

        # 현재 날짜는 최대 가격 날 다음 날이 됨
        date = price_i + 1

    return wallet


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_money = list(map(int, input().split()))
    print('#{} {}'.format(tc, millionaire(my_money)))