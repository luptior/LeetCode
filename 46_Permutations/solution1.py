def permute(nums: [int]) -> [[int]]:

    result = []

    def permute_with_rest(prev, rest):
        if not rest:
            result.append(prev)
        else:
            for x in rest:
                permute_with_rest(prev+[x], rest[:rest.index(x)]+rest[rest.index(x)+1:])

    permute_with_rest([], nums)

    return result


if __name__ == '__main__':
    nums = [0, 1]
    print(permute(nums))