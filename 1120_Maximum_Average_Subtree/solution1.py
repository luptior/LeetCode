# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max = 0

    def maximumAverageSubtree(self, root: TreeNode) -> float:

        self.maxAverageSubtree(root)

        return self.max

    def maxAverageSubtree(self, root: TreeNode):
        left, right = 10 ** 5 + 1, 10 ** 5 + 1
        l_count, r_count = 0, 0

        if root.left:
            left, l_count = self.maxAverageSubtree(root.left)

        if root.right:
            right, r_count = self.maxAverageSubtree(root.right)

        # curr average
        result = (left * l_count + right * r_count + root.val) / (l_count + r_count + 1)

        # update average
        self.max = max(self.max, result)

        return result, (l_count + r_count + 1)


if __name__ == '__main__':
    s = Solution()

    i = [5,6,1]

    print(s.maximumAverageSubtree())
