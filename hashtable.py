from linkedlist import TuplesLinkedList


class HashTable:

    def __init__(self):
        self.buckets = [TuplesLinkedList() for _ in range(17)]

    @staticmethod
    def hash_code(key):
        code_total = 0
        for i in range(len(key)):
            code_total += (ord(key[i]) * (31**i))
        return code_total

    def put(self, key, value):
        code = HashTable.hash_code(key)
        target_bucket = code % 17
        print(target_bucket)
        self.buckets[target_bucket].add(key, value)

    def get(self, key):
        code = HashTable.hash_code(key)
        target_bucket = code % 17
        print(self.buckets[target_bucket])
        return self.buckets[target_bucket].find(key)
