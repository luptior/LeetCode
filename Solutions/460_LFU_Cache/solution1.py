"""
untime: 3080 ms, faster than 5.04% of Python3 online submissions for LFU Cache.
Memory Usage: 23.6 MB, less than 87.98% of Python3 online submissions for LFU Cache.

"""


from collections import defaultdict
from collections import deque


class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.storage = {}
        self.key_freq = defaultdict(int)  # key to frq
        self.freq_key = defaultdict(list)  # freq to key

        # the most recent used will be added to the last
        self.time_order = deque([])

    def get(self, key: int) -> int:

        if key not in self.storage:
            return -1

        self.update_key(key)

        return self.storage[key]

    def update_key(self, key): # happen if the key is used

        # update key_freq
        tmp_freq = self.key_freq[key]
        self.key_freq[key] += 1

        # update freq_key
        self.freq_key[tmp_freq].remove(key)
        self.freq_key[tmp_freq + 1].append(key)

        # reorder the time needed
        k = self.time_order.index(key)
        self.time_order.remove(key)
        self.time_order.append(key)

    def remove_key(self): # remove a key

        # find the least used key set
        i = 0
        while not self.freq_key[i]:
            i += 1

        # sort the key set based on time_order and return the least recently used key
        key_to_remove = sorted(self.freq_key[i], key=lambda x: self.time_order.index(x))[0]

        del self.storage[key_to_remove]
        del self.key_freq[key_to_remove]  # key to frq
        self.freq_key[i].remove(key_to_remove)  # freq to key
        self.time_order.remove(key_to_remove)

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key not in self.storage:  # not already present

            if len(self.storage) >= self.capacity:  # full
                self.remove_key()

            # add key
            self.storage[key] = value

            self.key_freq[key] = 1
            self.freq_key[1].append(key)
            self.time_order.append(key)

        else:  # replace key
            # add key
            self.storage[key] = value

            self.update_key(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':

    c = None

    instr = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

    for i in range(len(instr)):
        if instr[i] == "LFUCache":
            c = LFUCache(*params[i])

        elif instr[i] == "put":
            c.put(*params[i])

            # print(instr[i], params[i], "Storage: ", c.storage, "freq_key: ", c.freq_key, "key_freq", c.key_freq, "time_order", c.time_order)

        elif instr[i] == "get":
            g = c.get(*params[i])

            print(g)

            # print(instr[i], params[i], "Storage: ", c.storage, "freq_key: ", c.freq_key, "key_freq", c.key_freq, "time_order", c.time_order)
