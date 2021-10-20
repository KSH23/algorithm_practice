# 18112. 이진수 게임


from collections import deque


def toggle(binary, idx):  # idx 위치를 보수로 바꾼 값 반환
    binary ^= (1 << idx)
    return binary


def binary_game():
    q = deque()
    q.append(start)  # 시작 지점 추가

    checked = [-1] * 1024
    checked[start] = 0  # 시작 지점 초기화
    path = [[] for _ in range((1 << 11) + 1)]  # 디버깅용 경로 저장 리스트
    while True:
        cur_num = q.popleft()  # 현재 이진수

        if cur_num == target:  # 목표 이진수 도착
            path[cur_num] += [cur_num]  # 디버깅용
            return checked[cur_num]

        for _ in range(3):
            # 한 자리 숫자를 보수로 바꾸기
            for i in range(len(bin(cur_num)) - 3):
                result = toggle(cur_num, i)
                if 1024 <= result:  # 1024 이상의 숫자는 나올 수 없음
                    continue
                if -1 < checked[result]:
                    continue  # 이미 확인한 숫자는 무시
                checked[result] = checked[cur_num] + 1  # 연산 횟수 갱신
                path[result] += path[cur_num] + [cur_num]  # 디버깅용
                q.append(result)

            # 현재 수에 1 더하기와 현재 수에서 1 빼기
            for delta in [-1, 1]:
                result = cur_num + delta
                if 1024 <= result:  # 1024 이상의 숫자는 나올 수 없음
                    continue
                if -1 < checked[result] or result < 0:
                    continue  # 이미 확인한 숫자 또는 음수 무시
                checked[result] = checked[cur_num] + 1  # 연산 횟수 갱신
                path[result] += path[cur_num] + [cur_num]  # 디버깅용
                q.append(result)


start = int(input(), 2)
target = int(input(), 2)
print(binary_game())
