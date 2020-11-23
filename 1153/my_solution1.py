# naive method, use index to check if conversion is possible.

def canConvert(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    if str1 == str2:
        return True

    s1 = {}
    s2 = {}
    for i, k in enumerate(str1):
        if k not in s1:
            s1[k] = [i]
        else:
            s1[k].append(i)

        if str2[i] not in s2:
            s2[str2[i]] = [i]
        else:
            s2[str2[i]].append(i)

    s1 = list(s1.values())
    s2 = list(s2.values())

    print(s1)
    print(s2)

    if len(s1) < len(s2):
        return False

    if len(s1) == len(s2) == 26:
        return False

    to_delete = []
    for i in range(len(s2)):
        if s2[i] in s1:
            s1.remove(s2[i])
            to_delete.append(s2[i])

    for x in to_delete:
        s2.remove(x)

    to_delete = []
    for x in s1:
        for i in range(len(s2)):
            if len(s2[i]) == 0: continue
            if all(element in s2[i] for element in x):
                to_delete.append(x)
                for element in x:
                    s2[i].remove(element)

    for x in to_delete:
        s1.remove(x)

    while [] in s2:
        s2.remove([])
    print(s1)
    print(s2)

    if len(s1) == len(s2) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "bcdefghijklmnopqrstuvwxyza"


    print(canConvert(str1, str2))
