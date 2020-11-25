# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):

        if not root:
            return []

        q = [[root, 1]]

        result = [[root.val]]

        while len(q) > 0:

            node = q.pop(0)

            # print(node[0].val, node[1] )

            if node[0].left:

                q.append([node[0].left, node[1] + 1])

                if node[1] == len(result):
                    result.append([node[0].left.val])
                else:
                    result[-1].append(node[0].left.val)

            if node[0].right:

                q.append([node[0].right, node[1] + 1])

                if node[1] == len(result):
                    result.append([node[0].right.val])
                else:
                    result[-1].append(node[0].right.val)

        return reversed(result)