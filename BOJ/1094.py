# 1094.막대기


X = int(input())
rod = [64]
rod_sum = 64
while rod_sum != X:
    shortest_rod = rod.pop()
    rod += [shortest_rod // 2, shortest_rod // 2]

    if rod_sum - shortest_rod // 2 >= X:
        rod.pop()
        rod_sum -= shortest_rod // 2

print(len(rod))