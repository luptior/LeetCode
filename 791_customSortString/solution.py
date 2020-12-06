# beat 98% python submission

def customSortString(S: str, T: str) -> str:

    unseen = []
    result = []

    for t in list(T):
        if t in S:
            result.append(t)
        else:
            unseen.append(t)

    result.sort(key = lambda x: S.index(x))

    result += unseen

    # print(T_key)

    return "".join(result)


if __name__ == '__main__':
    S = "cba"
    T = "abcd"

    print(customSortString(S, T))
