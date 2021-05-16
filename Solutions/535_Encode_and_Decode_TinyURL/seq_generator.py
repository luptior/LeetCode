"""
Runtime: 40 ms, faster than 14.37% of Python3 online submissions for Encode and Decode TinyURL.
Memory Usage: 14.4 MB, less than 15.79% of Python3 online submissions for Encode and Decode TinyURL.
"""


import math
from random import random


class Codec:

    def __init__(self):

        self.choice = [str(x) for x in range(10)] + \
                      [chr(x) for x in range(ord("A"), ord("Z") + 1)] + \
                      [chr(x) for x in range(ord("a"), ord("z") + 1)]

        self.store = {}

    def genSeq(self) -> str:

        if not self.store:
            return random.choice(self.choice)

        return "".join([random.choice(self.choice) for _ in range(int(math.log(len(self.store), self.choice)) + 1)])

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        seq = self.genSeq()

        while seq in self.store:
            seq = self.genSeq()

        self.store[seq] = longUrl

        return f"http://tinyurl.com/{seq}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        seq = shortUrl.split("/")[-1]

        return self.store[seq]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
