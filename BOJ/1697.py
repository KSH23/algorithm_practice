# 1697. 숨바꼭질


def check_number(num):
    # 들어온 위치 인자 num이 주어진 범위 내에 있는지 검사 후
    # 만약 가본 적 없는 길일 때 가도록 함
    if 0 <= num <= 100000 and number_line[num] == -1:
        number_line[num] = number_line[now] + 1
        q.append(num)


N, K = map(int, input().split())

number_line = [-1] * 100001
number_line[N] = 0
q = [N]    # 큐 생성

while True:
    now = q.pop(0)    # 현재 위치 X
    check_number(now - 1)    # X - 1로 이동
    check_number(now + 1)    # X + 1로 이동
    check_number(now * 2)    # 2 * X로 이동
    if now - 1 == K or now + 1 == K or now * 2 == K:
        break    # 동생을 잡으면 끝

print(number_line[K])