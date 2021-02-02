# TODO: list implement, TLE met

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.empties = []

    def push(self, val: int) -> None:
        if len(self.empties) > 0:
            self.stacks[self.empties.pop(0)] = val
        else:
            self.stacks.append(val)

    def pop(self) -> int:
        if not self.stacks: return -1
        while not self.stacks[-1]:
            if len(self.stacks) in self.empties:
                self.empties.remove(len(self.stacks))
            self.stacks.pop()
        return self.stacks.pop()

    def popAtStack(self, index: int) -> int:

        if index >= len(self.stacks)//self.capacity +1:
            return -1

        head = index*self.capacity

        result = -1

        for i in range(head + self.capacity-1, head-1, -1):
            if self.stacks[i]:
                if i < len(self.stacks) - 1:
                    result = self.stacks[i]
                    self.stacks[i] = None
                    self.addEmpty(i)
                    break
                else:
                    result = self.stacks[i]
                    self.stacks.pop()
                    break

        return result

    def addEmpty(self, index):
        if len(self.empties) < 3:
            self.empties.append(index)
            self.empties.sort()

        else:
            for i in range(len(self.empties)):
                if index <= self.empties[i]:
                    break
            self.empties = self.empties[:i] + [index] + self.empties[i:]


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

if __name__ == '__main__':
    D = DinnerPlates(1)
    print(D.push(1), D.stacks, D.empties)
    print(D.push(2), D.stacks, D.empties)
    print(D.popAtStack(1), D.stacks, D.empties)
    print(D.pop(), D.stacks, D.empties)
    print(D.push(1), D.stacks, D.empties)
    print(D.push(2), D.stacks, D.empties)
    print(D.pop(), D.stacks, D.empties)
    print(D.pop(), D.stacks, D.empties)