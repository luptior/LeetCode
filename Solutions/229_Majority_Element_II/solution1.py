from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        count1, count2, candidate1, candidate2 = 0, 0, None, None

        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                candidate1 = n
            elif count2 == 0:
                count2 += 1
                candidate2 = n
            else:
                count1 -= 1
                count2 -= 1

        result = []

        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)

        return result
