import sys


def word_finder(words: list) -> []:
    # preprocess by strip(), O(N)
    wordset = set([word.strip() for word in words])

    result = []

    for word in wordset:
        for i in range(1, len(word)):
            # print(word[:i], word[i:])
            if word[:i] in wordset and word[i:] in wordset:
                result.append(word)
                break

    return sorted(result)


if __name__ == '__main__':

    # read in stdin data
    data = sys.stdin.readlines()

    # a setting option: if input file has empty eof line, assume output file should have the same format
    endline_settings = "\n" in data[-1]

    result = word_finder(data)

    for i, e in enumerate(result):
        if i == len(result) - 1:
            print(e, end="\n" if endline_settings else '')
        else:
            print(e)
