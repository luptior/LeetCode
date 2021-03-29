import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius / 1
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1

        while x ** 2 + y ** 2 > 1:
            x = random.random() * 2 - 1
            y = random.random() * 2 - 1

        return [self.x_center + self.radius * x, self.y_center + self.radius * y]
