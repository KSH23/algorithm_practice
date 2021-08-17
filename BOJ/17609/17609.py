# 17609. 회문


def palindrome(s):
    start = 0
    end = len(s) -1
    flag = 0   # 유사회문을 체크하기 위한 변수
    start_here = end_here = 0    # 회문이 실패한 지점 저장

    while start <= end:
        if s[start] == s[end]:    # 앞뒤가 일치하면
            start += 1    # start에서 한 칸 앞과
            end -= 1    # end에서 한 칸 뒤를 검사

        else:    # 앞뒤가 일치하지 않을 때
            if flag == 0:    # 처음 걸린 것이라면
                start_here = start    # 걸린 지점 저장
                end_here = end    # 걸린 지점 저장
                flag += 1    # 걸린 횟수 추가
                start += 1    # 왼쪽을 한 칸 당긴 후 다시 시도
                continue
            elif flag == 1:    # 두번째 걸린 것이라면
                start = start_here    # 다시 되돌아가고
                end = end_here - 1    # 오른쪽을 한 칸 당긴 후 다시 시도
                flag += 1    # 걸린 횟수 추가
                continue
            elif flag == 2:    # 세번째 걸린 것이라면 끝
                return 2

    if flag == 0:    # 한번도 걸리지 않았다면 회문
        return 0
    else:    # 걸린 적 있다면 유사회문
        return 1


T = int(input())
for _ in range(T):
    S = input()
    print(palindrome(S))