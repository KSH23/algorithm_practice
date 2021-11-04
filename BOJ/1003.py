# 1003. 피보나치 함수


T = int(input())

# 리스트의 인덱스 == 원하는 숫자 N
# fibonacci_list[N][i. j]: i는 0의 출력 횟수, j는 1의 출력 횟수
fibonacci_list = [[0, 0] for _ in range(41)]
fibonacci_list[0] = [1, 0]
fibonacci_list[1] = [0, 1]

for num in range(2, 41):
    # 다음 숫자의 0과 1 출력 횟수는 이전과 그 이전 숫자의 0과 1 출력 횟수의 합과 같음
    fibonacci_list[num][0] = fibonacci_list[num - 1][0] + fibonacci_list[num - 2][0]
    fibonacci_list[num][1] = fibonacci_list[num - 1][1] + fibonacci_list[num - 2][1]

for _ in range(T):
    print(' '.join(map(str, fibonacci_list[int(input())])))