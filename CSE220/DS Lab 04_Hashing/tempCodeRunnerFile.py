class Node_pair:
    def __init__(self, key, value, next=None):
        self.key, self.value, self.next = key, value, next


class Hashtable:
    def __init__(self, size):
        self.ht = [None]*size

    def insert(self, s):
        hashed_index = self.__hash_function(s[0])
        pair = Node_pair(s[0], s[1])
        if self.ht[hashed_index] == None:
            self.ht[hashed_index] = pair
        else:
            pair.next = self.ht[hashed_index]
            self.ht[hashed_index] = pair

    def create_from_array(self, arr):
        for i in arr:
            self.insert(i)

    def print_hashtable(self):
        idx = 0
        for i in self.ht:
            print(idx, ':', end=' ')
            head = i
            while head != None:
                print(f'({head.key}, {head.value})', end='-->')
                head = head.next
            print('None')
            idx += 1

    # Do it by yourself
    def __hash_function(self, key):
        return (key + 3) % len(self.ht)

    # Do it by yourself
    def remove(self, key):
        for i in range(len(self.ht)):
            if self.ht[i] != None:
                temp = self.ht[i]
                if key == self.ht[i].key:
                    self.ht[i] = self.ht[i].next
                    return None
                while temp.next:
                    if temp.next.key == key:
                        temp.next = temp.next.next
                        return None
                    temp = temp.next



#Driver Code
arr=[(34, 'Abid') , (4, 'Rafi'), (6, 'Karim'), (3, 'Chitra'), (22, 'Nilu'), (18, 'Niloy'), (30, 'Laima')]
ht = Hashtable(6)
ht.create_from_array(arr)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (30, “Laima”) --> (18, “Niloy”) --> (6, “Karim”) --> None
#4: None
#5: None

print('======================')

ht.remove(22)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (30, “Laima”) --> (18, “Niloy”) --> (6, “Karim”) --> None
#4: None
#5: None

print('======================')

ht.remove(18)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (30, “Laima”) --> (6, “Karim”) --> None
#4: None
#5: None

print('======================')

ht.remove(6)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (30, “Laima”) --> None
#4: None
#5: None

print('======================')

ht.remove(3)
ht.print_hashtable()
#This should print

#0: None
#1: (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (30, “Laima”) --> None
#4: None
#5: None
