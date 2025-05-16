from PrettyPrint import PrettyPrintTree
import numpy as np
class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.left, self.right = None, None

def tree_construction(arr, i=1):
    if i >= len(arr) or arr[i] == None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p

class MinHeap:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__heapSize = 0
        self.__heap = np.full((self.__capacity + 1), None)
    
    def getHeap(self):
        return self.__heap

    def insert(self, elem):
        if self.__heapSize == self.__capacity:
            return "Heap is Full."
        self.__heapSize += 1
        self.__heap[self.__heapSize] = elem
        self.swim(self.__heapSize)
        return "Insertion Successful"

    def swim(self, idx):
        if idx <= 1 or self.__heap[idx // 2] < self.__heap[idx]:
            return
        self.__heap[idx], self.__heap[idx // 2]= self.__heap[idx // 2], self.__heap[idx]
        self.swim(idx // 2)

    def extractMin(self):
        if self.__heapSize == 0:
            return "No Element"
        self.__heap[self.__heapSize], self.__heap[1] = self.__heap[1], self.__heap[self.__heapSize]
        temp = self.__heap[self.__heapSize]
        self.__heap[self.__heapSize] = None
        self.__heapSize -= 1
        self.sink(1)
        return temp

    def sink(self, idx):
        left = 2 * idx
        right = (2 * idx) + 1
        if left > self.__heapSize:
            return
        elif right > self.__heapSize:
            if self.__heap[idx] < self.__heap[left]:
                return
            self.__heap[idx], self.__heap[left] = self.__heap[left], self.__heap[idx] 
        else:
            if (self.__heap[idx] < self.__heap[left] and self.__heap[idx] < self.__heap[right]):
                return
            smallest = left if self.__heap[left] < self.__heap[right] else right
            self.__heap[idx], self.__heap[smallest] = self.__heap[smallest], self.__heap[idx]
            self.sink(smallest)

    def sort(self):
        lostHeapSize = self.__heapSize
        def helper(heapSize, arr, idx = 0):
            if heapSize == 0:
                return arr
            arr[idx] = self.extractMin()
            return helper(heapSize - 1, arr, idx + 1)
        sorted_arr = helper(self.__heapSize, np.full(self.__heapSize, None))
        self.__heapSize = lostHeapSize
        return sorted_arr

#Driver Code
minHeap = MinHeap(11)
minHeap.insert(6)
minHeap.insert(5)
minHeap.insert(18)
minHeap.insert(11)
minHeap.insert(85)
minHeap.insert(20)
minHeap.insert(7)
minHeap.insert(23)
minHeap.insert(10)

#Tree Printer
children = lambda node: [child for child in (node.left, node.right) if child]
value = lambda node: str(node.elem)
tree_printer = PrettyPrintTree(children, value)

print("Before Min Extraction:")
tree = tree_construction(minHeap.getHeap())
print()
tree_printer(tree)

minHeap.extractMin()
print()

print("After Min Extraction:")
tree2 = tree_construction(minHeap.getHeap())
print()
tree_printer(tree2)

print()
print("Ascending Order HeapSort:")
print(minHeap.sort())