# 4831. 전기버스


T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    # list 안쓰고 그냥 바로 map()으로도 가능

    charging_spot = list(map(int, input().split()))
    station = [0] * (N+1)    # 정류장을 구현한 리스트
    for i in range(M):
        station[charging_spot[i]] = 1    # 충전기가 있다면 1을 넣음

    charge = K    # 현재 배터리
    x = 0    # 현재 위치
    cnt = 0    # 충전 횟수
    while x < N:
        if charge > 0:    # 아직 배터리가 남았다면
            x += 1        # 한 칸 앞으로 가고
            charge -= 1   # 배터리 한 칸 소모
        else:    # 배터리를 다 썼다면
            for i in range(K):
                if station[x-i] == 1:    # 충전기가 있는 정류장을 찾음
                    charge = K    # 충전
                    cnt += 1    # 충전 횟수 증가
                    x = x-i    # 충전기 위치로 이동
                    break
            if charge != K:    # 만약 충전하지 못했다면
                cnt = 0    # 충전 횟수 초기화(나중 출력을 위함)
                x = N+1    # 정류장 밖으로 나감

    print('#{} {}'.format(tc, cnt))