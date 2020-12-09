def multiply(num1: str, num2: str) -> str:

    s = 0
    for i, n2 in enumerate(num2):

        s += 10**(len(num2)-1-i)* sum([ 10**(len(num1)-1-j)* int(n2) * int(n1) for j, n1 in enumerate(num1)])

    return str(s)


if __name__ == '__main__':
    print(multiply(num1="123", num2="456"))