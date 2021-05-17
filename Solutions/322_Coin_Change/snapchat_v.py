"""
round 4: (day II) about 20min chat. Then a coding question: When you buy something in grocery, the cashier needs to pay
the change. Given the cashier has a register to keep all existing demonimations, write a method simulating how the
cashier finds all the denominations to pay the change. For example you paid $5 for something worth $2.35, the cashier
needs to find 2 $1, 6 dimes and 5 one cents if there are enough of these. You only need to find one solution and it's
possible there is no solution. It's an interesting problem. Once it's paid, the register needs to be updated. There
were lots of discussions. I did very well in this round.
"""
from functools import lru_cache


class Cashier:
    def __init__(self, register):

        self.register = register
        self.denominations = ()

    def change(self, price, paid):

        assert price <= paid

        if price == paid:
            return True

        else:
            change = paid - price

            @lru_cache
            def dfs(left, register, used):

                for i, d in enumerate(self.denominations):
                    if d < left and  register[i] > 0:

                        tmp_used = list(used)
                        tmp_used[i] += 1

                        tmp_register = list(register)
                        tmp_register[i] -= 1

                        tmp_left = left - d

                        dfs(tmp_left, tmp_register, tmp_used)

                        continue

                    if d == left:
                        tmp_used = list(used)
                        tmp_used[i] += 1

                        return tmp_used

            result = dfs(change, self.register, tuple())

            if result:
                return True














