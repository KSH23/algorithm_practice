def solution(line):
    points = set()  # 교점을 저장하는 세트
    
    for idx1 in range(len(line)):
        for idx2 in range(idx1 + 1, len(line)):
            a, b, e = line[idx1]  # 직선1
            c, d, f = line[idx2]  # 직선2
            
            # 분모가 0인 경우 넘어감
            parent = a * d - b * c  
            if not parent:
                continue
            
            child1 = b * f - e * d  # x 좌표의 분자
            child2 = e * c - a * f  # y 좌표의 분자
            if child1 % parent or child2 % parent:  # 교점의 좌표가 실수가 되는 경우
                continue
            
            points.add((child1 // parent, child2 // parent))
    
    # 교점의 범위를 정하기 위해 x와 y 좌표의 최대, 최소를 구함
    max_x, min_x = max(points)[0], min(points)[0]
    max_y, min_y = max(points, key=lambda x: x[1])[1], min(points, key=lambda x: x[1])[1]
    
    # 별이 그려지는 2차원 리스트
    answer = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    
    for x, y in points:
        answer[max_y - y][x - min_x] = "*"  # 위치 조절 후 별그리기
        
    for idx in range(len(answer)):
        answer[idx] = "".join(answer[idx])  # 출력 형식 맞춤
        
    return answer
    