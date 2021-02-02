# brute force

def countSmaller(self, nums: [int]) -> [int]:
    result = []

    for i, d in enumerate(nums):
        result.append(sum([0 if x >= d else 1 for x in nums[i + 1:]]))

    return result