# 6485. 삼성시의 버스 노선


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    routes = [list(map(int, input().split())) for _ in range(N)]    # 버스 노선
    
    P = int(input())
    stop = [0] * 5001    # 5천개의 버스 정류장
    stop_list = [int(input()) for _ in range(P)]    # 고려 대상 버스 정류장

    # 버스 노선에 속하는 버스 정류장을 인덱스로 이용하여 리스트 갱신
    for route in routes:
        for i in range(route[0], route[1]+1):
            stop[i] += 1

    # 버스 정류장을 인덱스로 이용하여 한 개씩 값을 출력
    print('#{}'.format(tc), end=' ')
    for i in stop_list:
        print('{}'.format(stop[i]), end=' ')
    print()
