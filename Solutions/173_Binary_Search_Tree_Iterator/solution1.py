# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.prevs = []  # stack
        self.curr = root
        self.curr_status = "in"
        self.next_status = "left"  # next is in

    def next(self) -> int:

        # print(self.curr, self.prevs)

        if self.curr_status == "in" and self.next_status == "left":

            if not self.curr.left:
                self.curr_status = "in"
                self.next_status = "right"
            else:

                while self.curr.left:
                    self.prevs.append(self.curr)
                    self.curr = self.curr.left

                self.curr_status = "left"
                self.next_status = "in"

        elif self.curr_status == "left" and self.next_status == "in":
            self.curr = self.prevs.pop()
            self.curr_status = "in"
            self.next_status = "right"

        elif self.curr_status == "in" and self.next_status == "right":
            self.curr = self.curr.right

            if not self.curr.left:
                self.curr_status = "in"
                self.next_status = "right"
            else:
                while self.curr.left:
                    self.prevs.append(self.curr)
                    self.curr = self.curr.left
                self.curr_status = "left"
                self.next_status = "in"

        return self.curr.val

    def hasNext(self) -> bool:

        if self.curr_status == "in" and self.next_status == "left":
            if self.curr or self.prevs: return True

        elif self.curr_status == "left" and self.next_status == "in":
            if self.prevs: return True

        elif self.curr_status == "in" and self.next_status == "right":
            if self.prevs or self.curr.right: return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()