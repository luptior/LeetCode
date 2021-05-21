import bisect
import collections


class Solution:
    def nextClosestTime(self, time: str) -> str:

        digits = set(list(time))
        digits.remove(":")
        digits = sorted(list(digits))

        result = collections.deque()

        result.extend(digits)

        tmp = result.popleft()
        for d in digits:
            result.append(tmp + d)

        while len(tmp) < 4:

            tmp = result.popleft()

            if len(tmp) == 4:
                result.appendleft(tmp)
                break

            for d in digits:
                result.append(tmp + d)

        result = [ int(x) for x in result]

        t = int("".join(time.split(":")))

        idx = bisect.bisect_left(result, t)

        print(idx, result[idx-1:idx+2], t)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.nextClosestTime("19:34"))