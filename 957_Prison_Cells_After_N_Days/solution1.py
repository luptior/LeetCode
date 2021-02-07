class Solution:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:

        if N == 0:
            return cells

        n = len(cells)
        storage = []
        tmp = cells[:]

        def update(idx: int):
            # update cell i's value in tmp based on cells
            if idx == 0 or idx == n - 1:  # right end
                tmp[idx] = 0
            else:
                tmp[idx] = int(cells[idx - 1] == cells[idx + 1])

        for i in range(N):
            for j in range(n):
                update(j)
            cells = tmp[:]

            if cells in storage:
                break
            else:
                storage.append(cells)

        N = N % len(storage)-1

        return storage[N]


if __name__ == '__main__':
    s = Solution()

    print(s.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 17))
