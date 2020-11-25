# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        q = [[root, 1]]

        depth = 1

        while len(q) > 0:

            node = q.pop(0)

            # print(node[0].val, node[1] )

            if node[0].left:
                q.append([node[0].left, node[1] + 1])

            if node[0].right:
                q.append([node[0].right, node[1] + 1])

            if not node[0].left and not node[0].right:
                # reach leaf
                if node[1] > depth:
                    depth = node[1]

        return depth