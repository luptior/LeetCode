# bfs, tle

from collections import deque


def minKnightMoves(x: int, y: int) -> int:

    x, y = abs(x), abs(y)
    # eight possible actions to go
    actions = [[1, 2], [2, 1], [2, -1], [1, -2], [-2, 1], [-1, 2]]

    wl = deque([[0, 0, 0]])
    visited = {(0, 0)}

    while wl:

        curr_x, curr_y, step = wl.popleft()
        for action in actions:
            new_pt = [curr_x + action[0], curr_y + action[1], step + 1]
            if tuple(new_pt[:2]) not in visited:
                visited.add(tuple(new_pt[:2]))
                if new_pt[:2] == [x, y]:
                    return new_pt[2]
                else:
                    wl.append(new_pt)


if __name__ == '__main__':
    print(minKnightMoves(1, 221))
