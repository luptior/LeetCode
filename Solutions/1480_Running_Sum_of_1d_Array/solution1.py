def runningSum(nums: [int]) -> [int]:
    result = []

    for i, num in enumerate(nums):
        if i == 0:
            result.append(num)
        else:
            result.append(result[-1] + num)

    return result


if __name__ == '__main__':
    print(runningSum([1,2,3,4]))