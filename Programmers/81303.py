# 81303. 표 편집


class Node:
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class LinkedList:
    def __init__(self, head, tail):
        self.head = Node(head)
        self.tail = Node(tail)

        self.head.next = self.tail
        self.tail.pre = self.head

        self.pointer = self.head  # 현재 노드

    def set_pointer(self, data):  # 현재 노드 설정
        for _ in range(data):
            self.pointer = self.pointer.next
        return self.pointer

    def move(self, direction, step):
        if direction == "U":
            for _ in range(step):
                self.pointer = self.pointer.pre
        else:
            for _ in range(step):
                self.pointer = self.pointer.next

    def append(self, data):
        pre_tail, new_tail = self.tail, Node(data)
        pre_tail.next = new_tail
        new_tail.pre = pre_tail
        self.tail = new_tail

    def insert(self, node):
        if node.pre:
            node.pre.next = node
        else:  # 현재 node가 head인 경우
            self.head = node
        if node.next:
            node.next.pre = node
        else:  # 현재 node가 tail인 경우
            self.tail = node

    def delete(self):
        if self.pointer == self.head:
            next_node = self.pointer.next
            next_node.pre = None
            self.head = next_node
            self.pointer = self.head

        elif self.pointer == self.tail:
            pre_node = self.pointer.pre
            pre_node.next = None
            self.tail = pre_node
            self.pointer = self.tail

        else:
            pre_node, next_node = self.pointer.pre, self.pointer.next
            pre_node.next = next_node
            next_node.pre = pre_node
            self.pointer = next_node


def solution(n, k, cmd):
    # 연결 리스트 초기 설정
    linked_list = LinkedList(0, 1)
    for name in range(2, n):
        linked_list.append(name)
    linked_list.set_pointer(k)

    recent_delete = []  # 삭제된 노드 저장 리스트
    for command in cmd:
        if 1 < len(command):
            move, step = command.split(" ")
            step = int(step)
            linked_list.move(move, step)

        elif command == "C":
            recent_delete.append(linked_list.pointer)
            linked_list.delete()

        else:
            deleted_node = recent_delete.pop()
            linked_list.insert(deleted_node)

    # 연결 리스트의 노드 개수와 n이 다를 수 있기 때문에 미리 X를 담아둔 리스트 생성
    result = ["X" for _ in range(n)]
    current_node = linked_list.head
    while current_node:
        result[current_node.data] = "O"
        current_node = current_node.next

    return "".join(result)
