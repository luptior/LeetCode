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


if __name__ == '__main__':
    s = [1,2,3,4,5,6,7,8]

    print(search(s, 4))