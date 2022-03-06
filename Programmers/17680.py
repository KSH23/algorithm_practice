from collections import deque


def solution(cacheSize, cities):
    answer = 0
    
    q = deque()

    for city in cities:
        city = city.lower()

        if city in q:  # cache hit
            # 참조 갱신
            q.remove(city)  
            q.append(city)
            answer += 1
            
        else:  # cache miss
            if q and len(q) == cacheSize:  # 다 찬 경우
                q.popleft()
            if cacheSize:  # 캐시 사이즈가 0이 아닐 때에만 추가
                q.append(city)
            answer += 5
    
    return answer