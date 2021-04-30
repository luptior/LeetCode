"""
Runtime: 20 ms, faster than 99.93% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.5 MB, less than 63.39% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
"""

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        wl = collections.deque([[root, (0, 0)]])

        d = collections.defaultdict(list)

        while wl:

            node, (level, col) = wl.popleft()

            if not node:
                continue

            d[col].append((level, node.val))

            if node.left:
                wl.append([node.left, (level + 1, col - 1)])

            if node.right:
                wl.append([node.right, (level + 1, col + 1)])

        d = {k: [x[1] for x in sorted(v)] for k, v in d.items()}

        return [d[i] for i in range(min(d.keys()), max(d.keys()) + 1)]
