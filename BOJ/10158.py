# 10158. 개미


def ant(w, h, p, q, t):
    w_t = t % (2 * w)   # 개미의 이동이 2W의 배수로 반복되므로 반복되는 시간 삭제
    h_t = t % (2 * h)   # 2H의 배수로 반복되는 시간 삭제

    # (w_t + p)와 w의 몫이 짝수이고 나머지가 x일때 p의 위치: x
    # (w_t + p)와 w의 몫이 홀수이고 나머지가 x일때 p의 위치: w - x
    # 이를 일반화 하면  p의 위치 = w * (짝수일때 0, 홀수일때 1) - x + 2x * (짝수일때 1, 홀수일때 0)
    p = w * (((w_t + p) // w) % 2) - ((w_t + p) % w) + 2 * ((w_t + p) % w) * (((w_t + p) // w + 1) % 2)
    q = h * (((h_t + q) // h) % 2) - ((h_t + q) % h) + 2 * ((h_t + q) % h) * (((h_t + q) // h + 1) % 2)

    return p, q


W, H = map(int, input().split())
P, Q = map(int, input().split())
T = int(input())
result = ant(W, H, P, Q, T)
print(result[0], result[1])