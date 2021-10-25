# 1629. 곱셈


def multiply(power_num):
    # 만약 이미 power_num만큼 제곱한 수의 나머지를 구했었다면
    # 그 값을 가져와 사용한다
    if power_num in remainders:
        return remainders[power_num]

    # power_num을 두 개의 숫자로 분할
    ret = multiply(power_num // 2)
    ret *= multiply((power_num + 1) // 2)

    # 해당 power_num에 대한 나머지를 저장
    remainders[power_num] = ret % C
    return ret % C


A, B, C = map(int, input().split())
remainders = {1: A % C}  # key: 제곱하는 횟수, value: 나머지
print(multiply(B))
