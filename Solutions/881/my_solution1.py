class Solution:
    def numRescueBoats(self, people, limit: int) -> int:

        rank = sorted(people, reverse=True)

        # result = []
        result = 0

        while len(rank) > 0:

            curr = rank.pop(0)

            if len(rank) == 0:
                # result.append(curr)
                result += 1
                break

            if curr > (limit - 1):
                # result.append(curr)
                result += 1

            else:
                if curr + rank[-1] > limit:
                    # # result.append(curr)
                    result += 1
                else:
                    # result.append([curr, rank.pop(-1)])
                    rank.pop(-1)
                    result += 1

        print(result)

        # return len(result)
        return result