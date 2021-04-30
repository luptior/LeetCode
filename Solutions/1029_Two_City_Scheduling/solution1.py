from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        costs.sort(key=lambda x: x[0] - x[1])

        return sum([cost[0] for cost in costs[:len(costs) // 2]]) + sum([cost[1] for cost in costs[len(costs) // 2:]])


