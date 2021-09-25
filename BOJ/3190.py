# 3190. 뱀


N = int(input())    # 보드의 크기
K = int(input())    # 사과의 개수

squares = [[0] * (N + 1) for _ in range(N + 1)]    # 보드
for apple in [list(map(int, input().split())) for _ in range(K)]:
    squares[apple[0]][apple[1]] = -1    # 보드에 사과 위치 표시

L = int(input())    # 뱀의 방향 변환 횟수
turns = [list(input().split()) for _ in range(L)]    # 방향 전환

# 현재 방향(인덱스)에서 우측, 좌측을 리스트로 저장
turn_list = [[1, 2], [3, 0], [0, 3], [2, 1]]
dr = [0, 1, -1, 0]    # 우하상좌
dc = [1, 0, 0, -1]    # 우하상좌

seconds = 0    # 지나간 초
head_r = head_c = 1    # 뱀 머리 위치 초기화
head_dir = tail = 0    # 뱀의 현재 방향과 꼬리의 값

turn = turns.pop(0)    # 첫 방향 전환 정보
turn_sec = int(turn[0])    # 첫 방향 전환 시간
rotate = turn[1]    # 첫 방향

while True:
    if turns and turn_sec < seconds:
        turn = turns.pop(0)    # 다음 방향 전환 정보 갱신
        turn_sec = int(turn[0])
        rotate = turn[1]

    if seconds == turn_sec:    # 방향 전환을 할 경우
        if rotate == 'D':    # 우측으로 방향 전환
            head_dir = turn_list[head_dir][0]
        else:    # 좌측으로 방향 전환
            head_dir = turn_list[head_dir][1]

    head_r += dr[head_dir]    # 다음 머리의 row 위치
    head_c += dc[head_dir]    # 다음 머리의 col 위치

    seconds += 1    # 시간 증가

    if head_r < 1 or head_c < 1 or N < head_r or N < head_c:
        break    # 보드를 벗어나면 끝

    if squares[head_r][head_c] >= tail:    
        if squares[head_r][head_c]:
            break    # 꼬리를 만나면 끝
        if head_r == 1 and head_c == 1 and tail == 0:
            break    # 꼬리와 머리가 (1, 1)에서 만날 경우

    tail += 1    # 꼬리 증가
    if squares[head_r][head_c] == - 1:
        tail -= 1    # 사과를 먹었다면 꼬리 유지

    squares[head_r][head_c] = seconds

print(seconds)