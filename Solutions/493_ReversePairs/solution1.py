# brute force, O(N^2)

class Solution1:
    def reversePairs(self, nums: [int]) -> int:

        result = []
        for i in range(len(nums)):

            result.append(sum([1 if nums[i] > 2*x else 0 for x in nums[i+1:]]))

        print(result)
        return sum(result)


# use dictionary, a little bit better

class Solution2:
    def reversePairs(self, nums: [int]) -> int:
        if len(nums) < 2: return 0

        d = {}

        count = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):

            if nums[i+1]*2 in d:
                d[nums[i+1]*2] += 1
            else:
                d[nums[i + 1] * 2] = 1

            count[i] = sum([ d[k] for k in d.keys() if k < nums[i]])

        # print(count)

        return sum(count)


if __name__ == '__main__':
    s = Solution2()

    print(s.reversePairs([1,3,2,3,1]))