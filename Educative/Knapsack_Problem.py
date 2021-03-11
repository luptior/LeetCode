class Solution:

    def __init__(self, weights, prices):
        self.weights = weights
        self.prices = prices
        self.mem = {}

    def knapsack_step(self, index, capacity):

        if capacity <= 0 or index >= len(self.weights):
            return 0

        elif (index, capacity) in self.mem:
            return self.mem[index, capacity]

        elif self.weights[index] > capacity:

            result = self.knapsack_step(index + 1, capacity)
            self.mem[index, capacity] = result
            return result

        else:

            result = max(self.prices[index] + self.knapsack_step(index + 1, capacity - self.weights[index]),
                       self.knapsack_step(index + 1, capacity))
            self.mem[index, capacity] = result
            return result

    def knapsack(self, capacity):
        # your code goes here

        return self.knapsack_step(0, capacity)


if __name__ == '__main__':
    weights = [1, 2, 4, 6]
    prices = [4, 2, 4, 7]
    capacity = 7

    s = Solution(weights, prices)

    print(s.knapsack(capacity))
