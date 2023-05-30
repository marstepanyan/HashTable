class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hashing(self, key):
        hash_value = 0
        for element in key:
            hash_value += ord(element)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hashing(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.hashing(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def display(self):
        for index in range(self.size):
            current = self.table[index]
            elements = []
            while current:
                elements.append(f"({current.key}: {current.value})")
                current = current.next
            print(f"{index}: {' -> '.join(elements)}")


ht = HashTable(10)
ht.insert('Mane', 110)
ht.insert('Mariam', 77)
ht.insert('naMe', 90)
ht.insert('ManeMane', 10)

print(ht.get('naMe'))
print(ht.get('Name'))

ht.display()

