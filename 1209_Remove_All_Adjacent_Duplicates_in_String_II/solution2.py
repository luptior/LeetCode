class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        count = []

        for c in s:
            if stack and stack[-1] == c:
                count[-1] += 1
                if k == count[-1]:
                    stack.pop()
                    count.pop()
            else:
                stack.append(c)
                count.append(1)

        return "".join([stack[i] * count[i] for i in range(len(stack))])