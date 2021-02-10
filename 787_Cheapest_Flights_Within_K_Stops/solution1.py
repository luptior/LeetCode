from collections import deque
import sys


class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:

        result = sys.maxsize

        wl = deque([])

        # at: 0, cost: 0, step: 0
        wl.append((src, 0, 0))

        while wl and wl[0][2] <= K:

            # print(result)

            node = wl.popleft()

            # print(node[0], dst, node[1] < result)

            if node[0] == dst and node[1] < result:
                # print(node[0], dst, node[1] < result)
                result = node[1]

                continue

            for candidate in [edge for edge in flights if edge[0] == node[0]]:
                if node[1] + candidate[2] < result:
                    wl.append((candidate[1], node[1] + candidate[2], node[2] + 1))

        if wl:
            tmp = [node[1] for node in wl if node[0] == dst]

            if tmp:
                tmp = min(tmp)

                if tmp < result:
                    result = tmp

        if result != sys.maxsize:
            return result
        else:
            return -1



