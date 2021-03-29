def calculation(operands):
    l = [int(o) if o.isnumeric() else o for o in operands]

    print(l)
    while "*" in l:
        i = l.index("*")
        l[i - 1] = l[i - 1] * l[i + 1]
        l.pop(i)
        l.pop(i)

    print(l)

    l = [o for o in l if o != "+"]

    while "-" in l:
        i = l.index("-")
        l[i + 1] = -l[i + 1]
        l.pop(i)

    return sum(l)


if __name__ == '__main__':

    for s in ["1*0+5"]:
        print(calculation(s))
