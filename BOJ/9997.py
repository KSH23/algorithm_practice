# 9997. 폰트


import sys


def dfs(start_idx, check):
    global ans

    if check == check_num:  # 만약 모든 알파벳을 넣었다면
        # 해당 결과를 포함하는 모든 부분집합의 개수를 추가
        ans += 2 ** (N - start_idx)
        return 1

    for idx in range(start_idx, N):
        next_check = check
        next_check = next_check | word_bit[idx]  # 알파벳 유무 확인

        if dfs(idx + 1, next_check):
            continue  # 모든 알파벳 포함된 경우를 만나고 돌아오는 경우


N = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

ord_a = ord('a')  # 상수 생성
check_num = (1 << 26) - 1  # 상수 생성

bit_masking = {}  # 비트마스킹 결과를 담을 딕셔너리
for ord_letter in range(ord('a'), ord('z') + 1):
    bit_masking[ord_letter] = 1 << (ord_letter - ord_a)

word_bit = [0] * (N+1)  # 각 단어의 비트연산 결과를 담을 리스트
for i in range(N):
    temp = 0
    for letter in words[i]:
        temp = temp | bit_masking[ord(letter)]
    word_bit[i] = temp

ans = 0  # 최종 정답
dfs(0, 0)
print(ans)