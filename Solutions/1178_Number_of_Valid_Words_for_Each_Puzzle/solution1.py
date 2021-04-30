"""
TLE solution

"""


from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        wordsSet = [set(list(word)) for word in words]
        puzzlesSet = [set(list(puzzle)) for puzzle in puzzles]

        result = [0] * len(puzzles)

        for i, puzzleSet in enumerate(puzzlesSet):

            for word in wordsSet:

                if puzzles[i][0] in word and not word - puzzleSet:
                    result[i] += 1

        return result