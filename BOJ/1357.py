# 1357. 뒤집힌 덧셈


def rev(num):
    result = 0    # 최종 결과
    ten = []    # 숫자를 뒤집어 저장할 리스트
    while num > 0:
        ten += [num % 10]    # 일의 자리 수 저장
        num //= 10    # 숫자의 자리 수를 줄임

    for i in range(len(ten)):
        # 리스트의 인덱스를 이용하여 10의 배수로 만듦
        result += 10 ** (len(ten) - 1 - i) * ten[i]

    return result


X, Y = map(int, input().split())
print(rev(rev(X) + rev(Y)))