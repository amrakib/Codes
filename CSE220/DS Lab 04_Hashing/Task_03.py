class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, length):
        n = Node()
        self.ht = [n] * length
        self.length = length

    def show(self):
        count = 0
        for i in self.ht:
            temp = i
            print(count, end=" ")
            while temp != None:
                print(temp.value, end="-->")
                temp = temp.next
            count += 1
            print()

    # Do it by yourself
    def __hash_function(self, key):
        i = 0 if len(key) % 2 == 0 else 1
        sum = 0
        for j in range(i, len(key), 2):
            sum += ord(key[j])
        return sum % self.length

    # Do it by yourself
    def insert(self, key, value):
        node = Node((key, value))
        index = self.__hash_function(key)
        if self.ht[index].value == None:
            self.ht[index] = node
        else:
            temp = self.ht[index]
            while temp:
                if temp.value[1] < value: 
                    node.next = self.ht[index]
                    self.ht[index] = node
                    return None
                elif temp.value[1] > value:
                    if temp.next == None:
                        temp.next = node
                        return None
                    elif temp.next.value[1] > value:
                        temp = temp.next
                    else:
                        node.next = temp.next
                        temp.next = node
                        return None

                
# Driver Code
ht = HashTable(3)

print("------Test#1------")
ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------Test#2------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()
print("------Test#3------")
ht.insert("apple", 100)
ht.insert("Guava", 10)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)--> ('pineapple', 50)--> ('banana', 30)-->
# 1 ('apple', 100)--> ('apple', 20)--> ('Guava', 10)-->
# 2 ('cherry', 50)-->
