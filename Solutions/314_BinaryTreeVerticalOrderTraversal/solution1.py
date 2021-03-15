"""

bfs solution

Runtime: 28 ms, faster than 94.09% of Python3 online submissions for Binary Tree Vertical Order Traversal.
Memory Usage: 14.3 MB, less than 51.97% of Python3 online submissions for Binary Tree Vertical Order Traversal.

"""


from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> [[int]]:

        if not root: return []

        wl = deque([[0, root]])

        d = defaultdict(list)

        while wl:
            ind, node = wl.popleft()
            d[ind].append(node.val)

            if node.left:
                wl.append([ind - 1, node.left])

            if node.right:
                wl.append([ind + 1, node.right])

        m = min(d.keys())

        return [list(d[k]) for k in range(m, m + len(d))]




if __name__ == '__main__':
    l = [3, 9, 20, None, None, 15, 7]

    head = TreeNode
