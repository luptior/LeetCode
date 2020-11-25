# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        l1 = []
        q1 = [p]

        l2 = []
        q2 = [q]

        while len(q1) > 0:

            node = q1.pop(0)

            if node is None:
                l1.append(None)
            else:
                l1.append(node.val)
                if node.left is None:
                    if node.right:
                        l1.append(None)
                else:
                    q1.append(node.left)

                if node.right:
                    q1.append(node.right)

        while len(q2) > 0:

            node = q2.pop(0)

            if node is None:
                l2.append(None)
            else:
                l2.append(node.val)
                if node.left is None:
                    if node.right:
                        l2.append(None)
                else:
                    q2.append(node.left)

                if node.right:
                    q2.append(node.right)

        return l1 == l2