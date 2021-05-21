"""
Runtime: 184 ms, faster than 37.33% of Python3 online submissions for Palindrome Permutation II.
Memory Usage: 25.6 MB, less than 8.53% of Python3 online submissions for Palindrome Permutation II.
"""

import collections
import itertools
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        d = collections.Counter(s)

        odd = {}
        even = {}
        wordset = []

        for k, v in d.items():

            if v % 2 == 0:
                even[k] = v
                for _ in range(even[k] // 2):
                    wordset.append(k)
            else:
                odd[k] = v

        # can not be palidromme
        if len(odd) > 1:
            return []
        elif len(odd) == 1:
            key = list(odd.keys())[0]
            val = list(odd.values())[0]
            if val > 1:
                for _ in range((val - 1) // 2):
                    wordset.append(key)

        tmp_result = set()

        for candidate in itertools.permutations(wordset, len(wordset)):
            tmp_result.add(tuple(candidate))

        result = []

        for tmp in tmp_result:
            result.append("".join(tmp) + (list(odd.keys())[0] if odd else "") + "".join(reversed(tmp)))

        return result









