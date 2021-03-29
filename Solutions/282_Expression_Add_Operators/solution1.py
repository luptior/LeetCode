from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        result = []

        def calculation(operands):

            l = [int(o) if o.isnumeric() else o for o in operands]

            while "*" in l:
                i = l.index("*")
                l[i - 1] == l[i - 1] * l[i + 1]
                l.pop(i)
                l.pop(i)

            l = [o for o in l if o != "+"]

            while "-" in l:
                i = l.index("-")
                l[i + 1] = -l[i + 1]
                l.pop(i)

            return sum(l)

        def step(index, operands):

            print(index, operands)

            if index == len(num) - 1:
                if calculation(operands) == target:
                    result.append(operands)

            # for operation in ['+', '-', '*']:
            if index < len(num) - 1:
                step(index + 1, operands + "+" + num[index + 1])
                step(index + 1, operands + "-" + num[index + 1])
                step(index + 1, operands + "*" + num[index + 1])

        step(0, num[0])

        return result


