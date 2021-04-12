import sys


def word_finder(words: list) -> []:
    """
    :param words: list of words in string format
    :return: list of compound words
    """

    # preprocess by strip(), O(N)
    words_set = set([word.strip() for word in words])

    result = []

    for word in words_set:
        for i in range(1, len(word)):
            # print(word[:i], word[i:])
            if word[:i] in words_set and word[i:] in words_set:
                result.append(word)
                break

    return sorted(result)


if __name__ == '__main__':

    # read in stdin data
    data = sys.stdin.readlines()

    # a setting option: if input file has empty eof line, assume output file should have the same format
    endline_settings = "\n" in data[-1]

    # use defined function to return the result
    result = word_finder(data)

    # print result to stdout, reformat last line based on input
    for i, e in enumerate(result):
        if i == len(result) - 1:
            print(e, end="\n" if endline_settings else '')
        else:
            print(e)
