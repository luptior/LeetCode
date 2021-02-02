# easy implement, TLE met

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []

    def push(self, val: int) -> None:


        if not self.stacks:
            self.stacks.append([val])
        else:
            pushed = False
            for i in range(len(self.stacks)):
                if len(self.stacks[i]) < self.capacity:
                    self.stacks[i].append(val)
                    pushed = True
                    break

            if not pushed:
                self.stacks.append([val])

    def pop(self) -> int:

        if not self.stacks:
            return -1

        while not self.stacks[-1]:
            self.stacks.pop()

        result = self.stacks[-1].pop()

        if not self.stacks[-1]:
            self.stacks.pop()

        return result

    def popAtStack(self, index: int) -> int:

        if index >= len(self.stacks):
            return -1

        if not self.stacks[index]:
            return -1

        result = self.stacks[index].pop()

        return result

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

if __name__ == '__main__':
    D = DinnerPlates(2)
    D.push(1)
    D.push(2)
    D.push(3)
    D.push(4)
    D.push(5)
    D.popAtStack(0)
    # print(D.stacks)
    D.push(20)
    # print(D.stacks)
    D.push(21)
    # print(D.stacks)
    print(D.popAtStack(0))
    print(D.popAtStack(2))