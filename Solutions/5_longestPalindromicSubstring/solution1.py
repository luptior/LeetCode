# brute force comparasion, TLE expected


def longestPalindrome(s: str) -> str:

    if len(s) < 10:
        result = ""
        max_ln = 0

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if j-i > max_ln and s[i:j] == "".join(reversed(s[i:j])):
                    result = s[i:j]
                    max_ln = len(s[i:j])

        return result

    if len(s) % 2 == 1:


def expendAroundCenter(s, L, R):
    while L >= 0 and R < len(s)


if __name__ == '__main__':

    print(longestPalindrome("babad"))