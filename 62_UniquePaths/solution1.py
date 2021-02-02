# dfs+memorization
# not optimal

class Solution:

    def __init__(self):
        self.mem = {}
        self.mem["1_1"] = 1

    def uniquePaths(self, m: int, n: int) -> int:
        if f"{m}_{n}" in self.mem: return self.mem[f"{m}_{n}"]

        result = self.uniquePaths(m - 1, n) if m > 1 else 0
        result += self.uniquePaths(m, n - 1) if n > 1 else 0

        self.mem[f"{m}_{n}"] = result

        return result