"""
recursive, TLE

"""


class Solution:

    def __init__(self):
        self.days = []
        self.costs = []

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.costs = costs

        return self.step(0, 0)

    @lru_cache(None)
    def step(self, curr_date, cost_so_far):

        if curr_date >= len(self.days):
            return cost_so_far

        c1 = self.step(curr_date + 1, cost_so_far + self.costs[0])

        new_days_left = self.days[curr_date:]
        end_date = new_days_left[0] + 6
        new_curr_date = curr_date

        while new_days_left and new_days_left[0] <= end_date:
            new_days_left.pop(0)
            new_curr_date += 1

        c2 = self.step(new_curr_date, cost_so_far + self.costs[1])

        new_days_left = self.days[curr_date:]
        end_date = new_days_left[0] + 29
        new_curr_date = curr_date

        while new_days_left and new_days_left[0] <= end_date:
            new_days_left.pop(0)
            new_curr_date += 1

        c3 = self.step(new_curr_date, cost_so_far + self.costs[2])

        return min(c1, c2, c3)
