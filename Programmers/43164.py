# 43164. 여행경로


from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for index, [depart, arrive] in enumerate(tickets):
        graph[depart].append((arrive, index))  # 도착 도시와 항공권 인덱스 기록
        graph[depart].sort()  # 알파벳 순 방문을 위한 처리

    # 사용한 항공권 표시
    used = [False] * len(tickets)

    def dfs(city, path):
        # 모든 항공권을 사용한 경우
        if len(path) == len(tickets) + 1:
            return path

        for next_city, ticket_index in graph[city]:
            if used[ticket_index]:
                continue

            # 사용할 수 있는 항공권 사용
            used[ticket_index] = True
            ret = dfs(next_city, path + [next_city])
            if ret:  # 가능한 경로가 존재할 경우 반환
                return ret
            used[ticket_index] = False

    return dfs("ICN", ["ICN"])
