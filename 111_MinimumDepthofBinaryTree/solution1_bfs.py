# Definition for a binary tree node.

import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        q = [[root, 1]]

        mini = sys.maxsize

        while q:

            node = q.pop()

            # print(not node[0].left , not node[0].right , node[1] < mini)

            if not node[0].left and not node[0].right and node[1] < mini:

                mini = node[1]

                if all([mini < x[1] for x in q]):
                    return mini

            if node[0].left:
                q.append([node[0].left, node[1] + 1])

            if node[0].right:
                q.append([node[0].right, node[1] + 1])

        return mini


