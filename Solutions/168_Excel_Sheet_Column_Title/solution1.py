import string

# unsolved

def convertToTitle(columnNumber: int) -> str:
    alphabet = list(string.ascii_uppercase)
    size = len(alphabet)
    result = ""

    while columnNumber > 0 :
        if columnNumber < size :
            result += alphabet[columnNumber-1]
            break
        p = int(columnNumber/size)
        r = columnNumber - p*size
        result += alphabet[p-1]
        columnNumber = r
    print(result)


if __name__ == '__main__':
    convertToTitle(2147483647)
