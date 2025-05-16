class Node:
    def __init__(self, vertex, weight):
        self.vertex = (vertex, weight)
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, end, weight):
        newNode = Node(end, weight)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode


nodes, edges = map(int, input().split())
source = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
weight = tuple(map(int, input().split()))

adj_list = [LinkedList() for _ in range(nodes + 1)]
adj_list[0] = None

for i in range(edges):
    adj_list[source[i]].add(end[i], weight[i])

for j in range(1, nodes + 1):
    print(f"{j}:", end=" ")
    temp = adj_list[j].head
    while temp:
        print(temp.vertex, end=" ")
        temp = temp.next
    print()
