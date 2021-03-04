from collections import deque


class Solution:
    def expand(self, s: str) -> [str]:

        candidates = []  # sorted list of results so far

        s = deque([x for x in list(s) if x != ","])

        # print(s)

        stack = []
        if_stack = False

        while s:

            curr = s.popleft()

            if curr == "{":
                if_stack = True

            elif curr == "}":
                if_stack = False
                stack = sorted(stack)

                if not candidates:
                    candidates = stack[:]
                else:

                    tmp = []
                    for candidate in candidates:
                        for element in stack:
                            tmp.append(f"{candidate}{element}")

                    candidates = tmp[:]

                stack = []

            else:
                if if_stack:
                    stack.append(curr)
                else:
                    if not candidates:
                        candidates.append(curr)
                    else:
                        tmp = []
                        for candidate in candidates:
                            tmp.append(f"{candidate}{curr}")

                        candidates = tmp[:]

            # print(candidates, curr, s)

        return candidates


if __name__ == '__main__':

    s = Solution()
    result = s.expand("{a,b}c{d,e}f")
    print(result)
    assert result ==  ["acdf", "acef", "bcdf", "bcef"]