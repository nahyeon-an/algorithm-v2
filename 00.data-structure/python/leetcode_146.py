from collections import OrderedDict


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node(key={self.key}, val={self.val})"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)


if __name__ == '__main__':
    obj = LRUCache(1)

    obj.put(2, 1)
    obj.get(2)
    obj.put(3, 2)
    obj.get(2)
    obj.get(3)

    # print(obj.get(2))
    # obj.put(2, 6)
    # print(obj.get(1))
    # obj.put(1, 5)
    # obj.put(1, 2)
    # print(obj.get(1))
    # print(obj.get(2))
    # obj.put(3, 2)
    # print(obj.get(1))
    # print(obj.get(3))

    # obj.put(1, 1)
    # obj.put(2, 2)
    # obj.get(1)
    # obj.put(3, 3)
    # obj.get(2)
    # obj.put(4, 4)
    # obj.get(1)
    # obj.get(3)
    # obj.get(4)