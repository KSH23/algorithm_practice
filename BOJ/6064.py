# 6064. 카잉 달력


T = int(input())
for tc in range(T):
    M, N, x, y = map(int, input().split())
    # x가 일치하는 년도를 찾은 후
    for year in range(x, M * N + 1, M):
        # y 값이 올바른지 검사 후 맞으면 출력
        if (year - y) % N == 0:
            print(year)
            break
    else:  # 일치하는 결과를 찾지 못한 경우
        print(-1)