"""

up-bottom
memorization

TLE

"""

class Solution:

    def __init__(self):

        self.nums1 = []
        self.nums2 = []
        self.k = 0
        self.mem = {}

    def maxNumber(self, nums1: [int], nums2: [int], k: int) -> [int]:

        self.nums1 = nums1
        self.nums2 = nums2
        self.k = k

        return self.step([], k, 0, 0)[0]

    def step(self, tmp_ans, k, index1, index2):

        if k == 0:  # reached the end
            return tmp_ans, int("".join([str(x) for x in tmp_ans]))

        if (k, index1, index2) in self.mem:
            seq = self.mem[(k, index1, index2)]

            n = "".join([str(x) for x in (tmp_ans + seq)])

            return tmp_ans + seq, int(n) if n.isnumeric() else 0

        if index1 >= len(self.nums1) and index2 >= len(self.nums2):
            return [], 0

        if index2 < len(self.nums2):
            # add one from nums2
            ans1, num1 = self.step(tmp_ans + [self.nums2[index2]], k - 1, index1, index2 + 1)
            self.mem[(k - 1, index1, index2 + 1)] = ans1[self.k - k + 1:]

            # not add, move to next from nums2
            ans4, num4 = self.step(tmp_ans, k, index1, index2 + 1)
            self.mem[(k, index1, index2 + 1)] = ans4[self.k - k:]
        else:
            ans1, num1 = [], 0
            ans4, num4 = [], 0

        if index1 < len(self.nums1):

            # add one from nums1
            ans2, num2 = self.step(tmp_ans + [self.nums1[index1]], k - 1, index1 + 1, index2)
            self.mem[(k - 1, index1 + 1, index2)] = ans2[self.k - k + 1:]

            # not add, move to next from nums1
            ans5, num5 = self.step(tmp_ans, k, index1 + 1, index2)
            self.mem[(k, index1 + 1, index2)] = ans5[self.k - k:]
        else:
            ans2, num2 = [], 0
            ans5, num5 = [], 0

        nums = [num1, num2, num4, num5]

        if nums.index(max(nums)) == 0:

            self.mem[(k, index1, index2)] = ans1[self.k - k:]
            return ans1, num1
        elif nums.index(max(nums)) == 1:

            self.mem[(k, index1, index2)] = ans2[self.k - k:]
            return ans2, num2
        elif nums.index(max(nums)) == 2:

            self.mem[(k, index1, index2)] = ans4[self.k - k:]
            return ans4, num4
        else:

            self.mem[(k, index1, index2)] = ans5[self.k - k:]
            return ans5, num5


if __name__ == '__main__':

    s = Solution()

    nums1 = [9, 1, 1, 0, 7, 8, 3, 9, 5, 3, 0, 7, 5, 7, 1, 8, 8, 3, 5, 7, 5, 2, 4, 7, 1, 2, 8, 9, 1, 6, 1, 1, 5, 6, 6, 1]
    nums2 =[6, 5, 5, 0, 0, 0, 3, 7, 7, 8, 0, 9, 7, 7, 3, 5, 1, 4, 5, 5, 4, 5, 2]
    k = 59

    print(s.maxNumber(nums1, nums2, k))