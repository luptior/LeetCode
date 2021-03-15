from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key not in self:
            return -1

        self.move_to_end(key)

        return self[key]

    def put(self, key: int, value: int) -> None:

        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':

    s = None

    instr = ["LRUCache", "put",  "put",  "get", "put",  "get", "put",  "get", "get", "get"]
    param = [[2],        [1, 1], [2, 2], [1],   [3, 3], [2],   [4, 4], [1],    [3],   [4]]


    for i in range(len(instr)):

        this_instr = instr[i]
        this_param = param[i]

        if this_instr == "LRUCache":
            s = LRUCache(this_param[0])
        elif this_instr == "put":
            k, v = this_param
            s.put(k,v)
        elif this_instr == "get":
            print(s.get(this_param[0]))
        else:
            print("Wrong")


