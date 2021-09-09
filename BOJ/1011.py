# 1011. Fly me to the Alpha Centauri


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    ans = 0    # 이동 횟수

    # 거리가 4 이상인 경우 x와 y 지점에서 서로 마주보며 점프하는 횟수를 셈
    # 첫 번째 점프는 한 칸, 두 번째 점프는 두 칸, ... 이하 동일
    arch = 1    # 점프 거리
    distance = y - x   # 거리

    # 점프는 양 옆에서 동시에 하기 때문에 현재 거리가 점프 * 2 보다 작으면 멈춤
    while 2 * arch <= distance:
        distance -= 2 * arch
        arch += 1    # 점프 거리 증가
        ans += 2    # 이동 횟수 증가(양 옆에서 한 번씩, 총 두번)

    # 점프 이후 남은 거리가 존재할 경우
    if distance > 0:
        # 만약 남은 거리가 점프보다 짧다면 한 번의 점프로 넘어갈 수 있음
        if arch >= distance:
            ans += 1
        else:
            ans += 2    # 그렇지 않다면 무조건 두 번의 점프로 넘어갈 수 있음

    print(ans)