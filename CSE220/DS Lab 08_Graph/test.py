import numpy as np
class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

# Creating a Graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacentMatrix = np.zeros((self.vertices, self.vertices), dtype=int)
        self.adjacentList = np.array([Node(i) for i in range(vertices)],dtype=object)
        

    def undrirected_matrix_connections(self, start, end):
        self.adjacentMatrix[start][end] = 1
        self.adjacentMatrix[end][start] = 1

    def directed_matrix_connections(self, start, end):
        self.adjacentMatrix[start][end] = 1


    def undirected_list_connections(self, start, end):
        head = self.adjacentList[start]
        temp = head.next
        head.next = Node(end)
        head.next.next = temp
        head = self.adjacentList[end]
        temp = head.next
        head.next = Node(start)
        head.next.next = temp

    def directed_list_connections(self, start, end):
        head = self.adjacentList[start]
        temp = head.next
        head.next = Node(end)
        head.next.next = temp

    def task_1_adjacencyMatrix(self):
        pass
            
        
#Creating a Undirected Graph Using Adjacent Matrix
undirected = Graph(7)
undirected.undrirected_matrix_connections(0, 1)
undirected.undrirected_matrix_connections(0, 3)
undirected.undrirected_matrix_connections(0, 5)
undirected.undrirected_matrix_connections(2, 4)
undirected.undrirected_matrix_connections(4, 6)
undirected.undrirected_matrix_connections(6, 2)
undirected.undrirected_matrix_connections(1, 2)
undirected.undrirected_matrix_connections(2, 3)
undirected.undrirected_matrix_connections(3, 4)
undirected.undrirected_matrix_connections(4, 5)
undirected.undrirected_matrix_connections(5, 6)
undirected.undrirected_matrix_connections(6, 1)
undirected.undrirected_matrix_connections(1, 3)
undirected.undrirected_matrix_connections(3, 5)
undirected.undrirected_matrix_connections(5, 1)
undirected.undrirected_matrix_connections(0, 4)
print("Undirected Adjacent Matrix Connections:\n", undirected.adjacentMatrix, end="\n\n")

#Creating a Undirected Graph Using Adjacent List
undirected.undirected_list_connections(0, 1)
undirected.undirected_list_connections(0, 3)
undirected.undirected_list_connections(0, 5)
undirected.undirected_list_connections(2, 4)
undirected.undirected_list_connections(4, 6)
undirected.undirected_list_connections(6, 2)
undirected.undirected_list_connections(1, 2)
undirected.undirected_list_connections(2, 3)
undirected.undirected_list_connections(3, 4)
undirected.undirected_list_connections(4, 5)
undirected.undirected_list_connections(5, 6)
undirected.undirected_list_connections(6, 1)
undirected.undirected_list_connections(1, 3)
undirected.undirected_list_connections(3, 5)
undirected.undirected_list_connections(5, 1)
undirected.undirected_list_connections(0, 4)
print("Undirected Adjacent List Connections:")
for i in range(undirected.vertices):
    ref = undirected.adjacentList[i]
    while ref != None:
        if ref.next:
            print(ref.elem, end="->")
        else:
            print(ref.elem)
        ref = ref.next
print()

#Creating a Directed Graph Using Adjacent Matrix
directed = Graph(7)
directed.directed_matrix_connections(0, 3)
directed.directed_matrix_connections(0, 1)
directed.directed_matrix_connections(0, 5)
directed.directed_matrix_connections(2, 4)
directed.directed_matrix_connections(4, 6)
directed.directed_matrix_connections(6, 2)
directed.directed_matrix_connections(1, 2)
directed.directed_matrix_connections(2, 3)
directed.directed_matrix_connections(3, 4)
directed.directed_matrix_connections(4, 5)
directed.directed_matrix_connections(5, 6)
directed.directed_matrix_connections(6, 1)
directed.directed_matrix_connections(1, 3)
directed.directed_matrix_connections(3, 5)
directed.directed_matrix_connections(5, 1)
directed.directed_matrix_connections(0, 4)
print("Directed Adjacent Matrix Connections:\n", directed.adjacentMatrix, end="\n\n")

#Creating a Directed Graph Using Adjacent List
directed.directed_list_connections(0, 1)
directed.directed_list_connections(0, 3)
directed.directed_list_connections(0, 5)
directed.directed_list_connections(2, 4)
directed.directed_list_connections(4, 6)
directed.directed_list_connections(6, 2)
directed.directed_list_connections(1, 2)
directed.directed_list_connections(2, 3)
directed.directed_list_connections(3, 4)
directed.directed_list_connections(4, 5)
directed.directed_list_connections(5, 6)
directed.directed_list_connections(6, 1)
directed.directed_list_connections(1, 3)
directed.directed_list_connections(3, 5)
directed.directed_list_connections(5, 1)
directed.directed_list_connections(0, 4)
print("Directed Adjacent List Connections:")
for i in range(directed.vertices):
    ref = directed.adjacentList[i]
    while ref != None:
        if ref.next:
            print(ref.elem, end="->")
        else:
            print(ref.elem)
        ref = ref.next
print()