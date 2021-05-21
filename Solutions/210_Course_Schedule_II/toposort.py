from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        neighbors = defaultdict(list)

        for dest, src in prerequisites:
            neighbors[src].append(dest)

        stack = []

        if_cyclic = False

        # 0 not visited, 1 visiting, 2 solved
        status = {k: 0 for k in range(numCourses)}

        # print(neighbors, status)

        def dfs(node):

            nonlocal if_cyclic

            if if_cyclic: return False

            status[node] = 1

            if node in neighbors:

                for neighbor in neighbors[node]:

                    if status[neighbor] == 0:
                        dfs(neighbor)
                    elif status[neighbor] == 1:
                        if_cyclic = True

            status[node] = 2

            stack.append(node)

        for node in range(numCourses):
            if status[node] == 0:
                dfs(node)

        return reversed(stack) if not if_cyclic else []