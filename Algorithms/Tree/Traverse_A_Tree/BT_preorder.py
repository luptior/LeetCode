class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> [int]:
        result = []
        if root:
            result = [root.val]

            if root.left: result += self.preorderTraversal(root.left)

            if root.right: result += self.preorderTraversal(root.right)

        return result