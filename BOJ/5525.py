# 5525. IOIOI


N = int(input())
S = int(input())
M = input()

length = 0  # 등장하는 IOI...OI의 길이
length_list = []  # 길이를 저장하는 리스트
idx = 0

while idx < S:
    # IOI 개수 세기 시작
    if M[idx] == 'I' and length == 0:
        length += 1
        idx += 1
        while idx < S:
            # O의 등장 위치는 문자열의 길이가 홀수일 때
            if M[idx] == 'O' and length % 2:
                length += 1
                idx += 1
            else:  # 문자열 규칙이 어긋난 경우
                length_list.append(length)
                length = 0
                break

            # I의 등장 위치는 문자열의 길이가 짝수일 때
            if idx < S and M[idx] == 'I' and not length % 2:
                length += 1
                idx += 1
            # 문자열 규칙이 어긋난 경우 마지막 문자가 O라서 길이는 1 뺌
            else:
                length_list.append(length - 1)
                length = 0
                break
    else:
        idx += 1

if length:  # IOI로 끝나는 경우 대비
    length_list.append(length)

ans = 0  # 최종 정답
for length in length_list:
    # 문자열 P_M에 들어있는 P_N의 개수는 (M - N) + 1
    P_M = (length - 1) // 2
    if N <= P_M:
        ans += P_M - N + 1
print(ans)