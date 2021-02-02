# TODO

from collections import deque


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        d = self.recur_count(formula)

        return "".join([f"{k}{d[k]}" if d[k] > 1 else k for k in sorted(d.keys())])

    def recur_count(self, formula) -> dict:
        if "(" not in formula:
            d = self.plain_count(formula)
        else:

            d  = {}
            s1 = ""
            s2 = ""
            stack = []

            for c in formula:
                print("unsolved")


        return d

    def plain_count(self, formula) -> dict:
        d = {}

        element_name = ""
        count = ""

        for i, c in enumerate(formula):
            if c.isupper():
                element_name = c

                # print(i < len(formula) - 1,  formula[i + 1].isupper(), i == len(formula) - 1)
                if i < len(formula) - 1 and formula[i + 1].isupper() or i == len(formula) - 1:
                    # if not element_name: print("path1")
                    if element_name in d:
                        d[element_name] += 1
                    else:
                        d[element_name] = 1
                    element_name = ""
                # else: either lower case or number followed
            elif c.islower():
                element_name += c

                if i < len(formula) - 1 and formula[i + 1].isupper() or i == len(formula) - 1:
                    # if not element_name: print("path2")
                    if element_name in d:
                        d[element_name] += 1
                    else:
                        d[element_name] = 1
                    element_name = ""

            elif c.isnumeric():
                count += c
                if i < len(formula) - 1 and formula[i + 1].isnumeric():  # next is numeric
                    continue
                else:  # either end or other things
                    # print(element_name)
                    if not element_name:
                        print(formula)
                        # print("path3")
                    if element_name in d:
                        d[element_name] += int(count)
                    else:
                        d[element_name] = int(count)
                    count = ""
                    element_name = ""

            # print(i, c, element_name, count, d)

        return d

    def merge(self, d1: dict, d2: dict):

        for k in d2.keys():
            if k in d1:
                d1[k] += d2[k]
            else:
                d1[k] = d2[k]

        return d1


if __name__ == '__main__':
    formula = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
    # formula = "SO3"
    s = Solution()
    print(s.countOfAtoms(formula))

    # print(s.plain_count("Mg"))
