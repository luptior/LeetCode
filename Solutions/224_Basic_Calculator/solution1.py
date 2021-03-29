class Solution:
    def calculate(self, s: str) -> int:

        if not "(" in s:
            l = [c for c in list(s) if c != " "]

            for i, d in enumerate(l):
                if d == "-":
                    l[i + 1] = "-" + l[i + 1]

            l = [int(c) for c in l if c != "-"]

            return sum(l)

        stack = 0
        sign = ""
        inner = ""

        flatten = ""
        result = 0

        for c in s:

            if c == "(" and stack == 0:
                stack += 1
                if not flatten or flatten[-1] == "+":
                    sign = "+"
                else:
                    sign = "-"
                if flatten:
                    flatten = flatten[:-1]
            elif c == "(" and stack:
                stack += 1
                inner += c
            elif c == ")" and stack:
                stack -= 1
                if stack == 0:
                    tmp = self.calculate(inner)
                    if sign == "+":
                        result += tmp
                    else:
                        result -= tmp
                    continue
                inner += c
            else:
                flatten += c

        result += self.calculate(flatten)

        return result


if __name__ == '__main__':

    print(Solution().calculate("2147483647"))

