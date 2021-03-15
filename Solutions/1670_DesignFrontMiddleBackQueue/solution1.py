from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):

        self.d = deque([])

    def pushFront(self, val: int) -> None:
        self.d.appendleft(val)

    def pushMiddle(self, val: int) -> None:

        m = len(self.d) // 2

        l = list(self.d)

        l = l[:m] + [val] + l[m:]

        self.d = deque(l)

    def pushBack(self, val: int) -> None:
        self.d.append(val)

    def popFront(self) -> int:
        if not self.d: return -1

        return self.d.popleft()

    def popMiddle(self) -> int:

        m = len(self.d) // 2

        l = list(self.d)

        result = l[m]

        l = l[:m] + l[m + 1:]

        self.d = deque(l)

        return result

    def popBack(self) -> int:
        if not self.d: return -1

        return self.d.pop()

if __name__ == '__main__':

    # Your FrontMiddleBackQueue object will be instantiated and called as such:
    obj = FrontMiddleBackQueue()
    obj.pushFront(1)
    obj.pushMiddle(2)
    obj.pushBack(3)
    param_4 = obj.popFront()
    param_5 = obj.popMiddle()
    param_6 = obj.popBack()