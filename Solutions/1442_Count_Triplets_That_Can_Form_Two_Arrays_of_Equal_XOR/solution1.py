class Solution:

    def __init__(self):

        self.result = 0

    def countTriplets(self, arr: [int]) -> int:
        self.countNextStep([], arr)
        return self.result

    def if_valid(self, arr: [int]):
        if len(arr) != 3:
            return

        if (arr[0] > arr[1] > arr[2]) or (arr[0] < arr[1] < arr[2]):
            self.result += 1

    def countNextStep(self, prev, left):

        if len(prev) > 3 or len(prev) < 3 and not left:
            return

        if len(prev) == 3:
            # print(prev, left, self.result)
            self.if_valid(prev)
            return

        for i, element in enumerate(left):
            self.countNextStep(prev+[element], left[i+1:])


if __name__ == '__main__':
