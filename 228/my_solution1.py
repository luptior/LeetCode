class Solution:
    def summaryRanges(self, nums) :

        if len(nums) == 0:
            return []

        full = set(range(nums[0], nums[-1] + 1))

        break_points = full - set(nums)

        result = []

        prev = nums[0]

        for bp in break_points:

            if prev < bp - 1:
                result.append(f"{prev}->{bp - 1}")
            else:
                result.append(f"{prev}")
            prev = bp + 1

        if prev < nums[-1]:
            result.append(f"{prev}->{nums[-1]}")
        else:
            result.append(f"{nums[-1]}")

        return result