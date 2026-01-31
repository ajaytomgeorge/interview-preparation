# approach via simple collision handling via Separate Chaining


class HashTable():
    def __init__(self, size):
        self.size = size
        self.array = [[] for _ in range(size)]

    def insert(self, key, value):
        index = hash(key)% self.size

        for i, (current_key, current_value) in enumerate(self.array[index]):
            print("Collsion:", self.array[index])
            if key == current_key:
                self.array[index][i] = (key, value)
                return
        self.array[index].append( (key, value))
    
    def get(self, key):
        index = hash(key)% self.size
        for i, (current_key, current_value) in enumerate(self.array[index]):
            if key ==current_key:
                return current_value


        

a = HashTable(8)
a.insert(1, 'apple')
a.insert(2, 'banana')
a.insert(4, 'rasberry')
a.insert(12, 'strawberry')

print(a.get(1))
print(a.get(2))
print(a.get(4))
print(a.get(12))
print(a.get(13))


#Option B: Open Addressing (linear probing)

def put(key, value):
    index = hash_function(key)

    while table[index] is not None:
        if table[index][0] == key:
            table[index] = (key, value)
            return
        index = (index + 1) % size

    table[index] = (key, value)


    def get(key):
    index = hash_function(key)

    while table[index] is not None:
        if table[index][0] == key:
            return table[index][1]
        index = (index + 1) % size

    return None
