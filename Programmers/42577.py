# 42577. 전화번호 목록


def solution(phone_book):
    phone_book.sort()

    for idx in range(len(phone_book) - 1):
        # 현재 번호와 다음 번호의 첫 자리 숫자가 같은 경우 탐색 진행
        if phone_book[idx][0] == phone_book[idx + 1][0]:
            # 현재 번호와 다음 번호의 각 숫자를 비교
            for inner_idx in range(1, len(phone_book[idx])):
                if phone_book[idx][inner_idx] != phone_book[idx + 1][inner_idx]:
                    break
            # 만약 모든 숫자가 중단 없이 비교 완료되었다면
            # phone_book[idx]는 phone_book[idx + 1]의 접두어
            else:
                return False

    # 어떤 번호가 다른 번호의 접두어인 경우가 없는 경우
    return True