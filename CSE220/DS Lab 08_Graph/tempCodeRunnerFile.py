            head = self.adjacentList[end]
            temp = head.next
            head.next = Node(start)
            head.next.next = temp