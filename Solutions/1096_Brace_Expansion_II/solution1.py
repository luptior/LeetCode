from collections import deque


class Solution:
    def braceExpansionII(self, s: str) -> [str]:

        candidates = []  # sorted list of results so far




if __name__ == '__main__':

    s = Solution()
    result = s.braceExpansionII("{a,b}{c,{d,e}}")
    print(result)
    assert result == ["ac","ad","ae","bc","bd","be"]