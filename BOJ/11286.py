# 11286. 절댓값 힙


"""
힙을 구현해보기 위해 참고자료를 이용해 작성하였다.
참고자료 1. https://www.fun-coding.org/Chapter11-heap.html
참고자료 2. https://velog.io/@swimme/Python-Heap
참고자료 3. https://daimhada.tistory.com/108
"""


import sys


class MinHeap(object):

    def __init__(self):
        self.queue = [(0, 0)]  # 1번 인덱스부터 사용

    def insert(self, item):
        self.queue.append(item)  # 마지막에 원소 삽입
        index = len(self.queue) - 1

        # 루트노드까지 탐색하며 만약 부모가 현재 index 노드보다 크다면 swap
        while 1 < index:
            if self.queue[index][0] < self.queue[index // 2][0]:
                self.queue[index // 2], self.queue[index] = self.queue[index], self.queue[index // 2]
                index //= 2

            # 절댓값이 같은 경우 초기 숫자를 비교한 뒤 swap
            elif self.queue[index][0] == self.queue[index // 2][0]:
                if self.queue[index][1] < self.queue[index // 2][1]:
                    self.queue[index // 2], self.queue[index] = self.queue[index], self.queue[index // 2]
                index //= 2
            else:
                break

    def delete(self):
        index = len(self.queue) - 1
        if index == 0:  # 힙이 비어있다
            return 0

        # 루트 노드(최솟값)와 마지막 노드 swap
        self.queue[1], self.queue[index] = self.queue[index], self.queue[1]
        min_value = self.queue.pop()  # 최솟값 제거
        self.min_heapify(1)  # 새로운 루트 노드부터 재정렬
        return min_value[1]

    def min_heapify(self, root_index):  # 힙 재정렬
        left_child_index = 2 * root_index
        right_child_index = 2 * root_index + 1
        smallest_index = root_index  # 최솟값을 갖는 노드의 인덱스

        # 왼쪽 자식이 존재하고 그 자식이 현재 root보다 작은 값인 경우 인덱스 갱신
        if left_child_index < len(self.queue):
            if self.queue[left_child_index][0] < self.queue[smallest_index][0]:
                smallest_index = left_child_index

            # 절댓값이 같은 경우 더 작은 수를 선택
            elif self.queue[left_child_index][0] == self.queue[smallest_index][0]:
                if self.queue[left_child_index][1] < self.queue[smallest_index][1]:
                    smallest_index = left_child_index

        # 오른쪽 자식이 존재하고 그 자식이 현재 root보다 작은 값은 경우 인덱스 갱신
        if right_child_index < len(self.queue):
            if self.queue[right_child_index][0] < self.queue[smallest_index][0]:
                smallest_index = right_child_index

            # 절댓값이 같은 경우 더 작은 수를 선택
            elif self.queue[right_child_index][0] == self.queue[smallest_index][0]:
                if self.queue[right_child_index][1] < self.queue[smallest_index][1]:
                    smallest_index = right_child_index

        if smallest_index != root_index:  # 인덱스가 갱신된 경우 swap
            self.queue[root_index], self.queue[smallest_index] = self.queue[smallest_index], self.queue[root_index]
            self.min_heapify(smallest_index)  # 이하 서브 트리 재정렬


N = int(sys.stdin.readline())
min_heap = MinHeap()
for _ in range(N):
    command = int(sys.stdin.readline())
    if command != 0:
        min_heap.insert((abs(command), command))
    else:
        print(min_heap.delete())