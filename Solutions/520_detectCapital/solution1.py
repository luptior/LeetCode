def detectCapitalUse(word: str) -> bool:

    if len(word) == 0: return False

    if word[0].isupper():
        return all(x.isupper() for x in word[1:]) or all(x.islower() for x in word[1:])
    else:
        return all(x.islower() for x in word[1:])


if __name__ == '__main__':
    print(detectCapitalUse("F"))