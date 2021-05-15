import collections
from bisect import bisect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.storage = collections.defaultdict(collections.OrderedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        k = bisect.bisect_left(list(self.storage[key].keys()), timestamp)

        print(k, self.storage[key])

        return self.storage[key][list(self.storage[key].keys())[k]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)