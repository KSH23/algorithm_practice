# 87946. 피로도


def solution(k, dungeons):
    visited = [False] * len(dungeons)  # 던전 방문 기록
    
    def go_dungeon(heart):
        ret = 0  # 방문한 던전의 수
        for idx in range(len(dungeons)):
            if visited[idx]:  # 방문한 적 있는 던전은 무시
                continue
            visited[idx] = True  # 방문 표시
            if dungeons[idx][0] <= heart:  # 최소 필요 피로도가 남은 경우 던전 입장
                ret = max(ret, go_dungeon(heart - dungeons[idx][1]) + 1)
            visited[idx] = False  # 방문 표시 해제
        return ret

    return go_dungeon(k)