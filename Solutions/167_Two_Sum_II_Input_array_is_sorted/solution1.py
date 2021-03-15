# naive 

class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:

        # result = []

        for i in range(len(numbers)):

            if target-numbers[i] >= numbers[i] and target-numbers[i] in numbers[i+1:]:

                return [i+1, numbers[i+1:].index(target-numbers[i])+1+i+1]

if __name__ == '__main__':

    s = Solution()

    numbers = [2,7,11,15]
    target = 9

    print(s.twoSum(numbers, target))