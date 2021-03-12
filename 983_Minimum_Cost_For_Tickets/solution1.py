"""
recursive, TLE

"""

class Solution:

    def __init__(self):
        self.days = []
        self.costs = []

        self.mem = {}

    def mincostTickets(self, days: [int], costs: [int]) -> int:
        self.days = days
        self.costs = costs

        self.mem = {}

        result = self.step(days, 0)

        print(self.mem)

        return result

    def step(self, days_left, cost_so_far):

        if not days_left:
            return cost_so_far

        c1 = self.step(days_left[1:], cost_so_far + self.costs[0])

        new_days_left = days_left[:]
        end_date = new_days_left[0] + 6

        while new_days_left and new_days_left[0] <= end_date:
            new_days_left.pop(0)

        c2 = self.step(new_days_left, cost_so_far + self.costs[1])

        new_days_left = days_left[:]
        end_date = new_days_left[0] + 29

        while new_days_left and new_days_left[0] <= end_date:
            new_days_left.pop(0)

        c3 = self.step(new_days_left, cost_so_far + self.costs[2])

        return min(c1, c2, c3)
