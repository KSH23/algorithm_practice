# 5014. 스타트링크


floors, start, goal, up, down = map(int, input().split())

elevator = [-1] * (floors + 1)    # 최소로 눌러야 하는 횟수 저장 리스트
elevator[start] = 0    # 현재 있는 층을 0으로 설정
queue = [start]    # 큐 생성하고 현재 층 담음

while len(queue) > 0:    # BFS 실행
    now = queue.pop(0)

    # 만약 up 버튼을 누를 수 있고 (now + up)층에 가본 적 없다면
    # 현재 횟수에 1을 더한 값을 다음 층에 넣고 큐에 저장
    if now + up <= floors and elevator[now + up] == -1:
        elevator[now + up] = elevator[now] + 1
        queue += [now + up]

    # down 버튼의 경우도 위와 동일
    if now - down > 0 and elevator[now - down] == -1:
        elevator[now - down] = elevator[now] + 1
        queue += [now - down]

ans = elevator[goal]    # 눌러야 하는 횟수의 최솟값
if ans == -1:    # 만약 이 값이 -1이라면 갈 수 없음
    print('use the stairs')
else:
    print(ans)