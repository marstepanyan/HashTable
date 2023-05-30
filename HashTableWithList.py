class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = []

        for i in range(self.size):
            self.table.append([])

    def hashing(self, key):
        hash_value = 0
        for element in key:
            hash_value += ord(element)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hashing(key)
        self.table[index].append([(key, value)])

    def get(self, key):
        index = self.hashing(key)
        if self.table[index]:
            for item in self.table[index]:
                for pair in item:
                    if pair[0] == key:
                        return pair[-1]
        return

    # def __repr__(self):
    #     res = []
    #     for i in range(self.size):
    #         res.append(self.table[i])
    #         print(f"{i}: {res[i]}")

    def display(self):
        elements = []
        for index in range(self.size):
            for item in self.table[index]:
                elements.append(f'{item[0][0]}:{item[0][-1]}')

            print(f"{index}: {' , '.join(elements)}")
            elements = []


ht = HashTable(20)
ht.insert('Mane', 110)
ht.insert('Mariam', 77)
ht.insert('naMe', 90)

print(ht.get('naMe'))
print(ht.get('Name'))

ht.display()
