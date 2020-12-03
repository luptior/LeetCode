# brute force comparasion, TLE expected


def longestPalindrome(s: str) -> str:

    result = ""
    max_ln = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j-i > max_ln and s[i:j] == "".join(reversed(s[i:j])):
                result = s[i:j]
                max_ln = len(s[i:j])

    return result


if __name__ == '__main__':

    print(longestPalindrome("babad"))