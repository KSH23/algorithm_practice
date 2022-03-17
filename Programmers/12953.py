# 12953. N개의 최소공배수


def find_gcd(num1, num2):
    """
    유클리드 호제법을 이용하여 최소공약수 반환
    """
    num1, num2 = max(num1, num2), min(num1, num2)
    if num1 % num2 == 0:
        return num2
    ret = find_gcd(num2, num1 % num2)
    return ret


def solution(arr):
    # 최소공배수, 최대공약수의 초기값 설정
    lcm, gcd = arr[0], arr[0]
    
    for number in arr[1:]:
        # 새로운 숫자와의 최대공약수를 갱신
        gcd = find_gcd(lcm, number)
        
        # 갱신된 최대공약수를 이용해 최소공배수 갱신
        lcm = gcd * (lcm // gcd) * (number // gcd)

    return lcm
