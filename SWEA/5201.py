# 5201. 컨테이너 운반


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    weights.sort(reverse=True)  # 내림차순 정렬
    trucks.sort(reverse=True)  # 내림차순 정렬

    idx = 0  # 화물 인덱스
    ans = 0
    for truck in trucks:
        while idx < N and truck < weights[idx]:
            idx += 1

        if N <= idx:
            break

        ans += weights[idx]
        idx += 1

    print(f'#{tc} {ans}')