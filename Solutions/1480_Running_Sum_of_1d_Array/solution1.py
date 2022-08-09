def runningSum(nums: [int]) -> [int]:


    ## 1
    # result = []
    #
    # for i, num in enumerate(nums):
    #     if i == 0:
    #         result.append(num)
    #     else:
    #         result.append(result[-1] + num)
    #
    # return result

    ## 2
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]

    return nums


if __name__ == '__main__':
    print(runningSum([1,2,3,4]))