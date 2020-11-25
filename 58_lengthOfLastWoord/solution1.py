class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if " " not in s:
            return len(s)

        new_s = ""

        for i, c in enumerate(s):

            # print(i, f"|{c}|",  c == " ")
            if i > 0:
                if c == " " and s[i - 1] != c:
                    new_s += c
                elif c != " ":
                    new_s += c
            else:
                new_s += c

        # print(new_s)

        last = new_s.split(" ")[-1] if len(new_s.split(" ")[-1]) > 0 else new_s.split(" ")[-2]

        return len(last)