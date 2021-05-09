import bisect


def search(arr, target):

    left = 0
    right = len(arr) - 1

    while left < right:

        mid = (left + right) //2

        if arr[mid] < target:
            left = mid
        elif arr[mid] > target:
            right = mid
        else:
            return mid

def search2(arr, target):

    return bisect.bisect_left(arr, target)


if __name__ == '__main__':
    s = [1,2,3,5,6,7,8]

    print(search2(s, 5))