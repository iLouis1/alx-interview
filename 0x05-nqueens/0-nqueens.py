#!/usr/bin/python3
'''The N Queens Challenge'''

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        k = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if k < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = []  # coordinates format [row, column]
    stop = False
    j = 0
    c = 0

    # iterate thru rows
    while j < k:
        goback = False
        # iterate thru columns
        while c < k:
            # check is current column is safe
            safe = True
            for cord in placed_queens:
                col = cord[1]
                if(col == c or col + (r-cord[0]) == c or
                        col - (r-cord[0]) == c):
                    safe = False
                    break

            if not safe:
                if c == k - 1:
                    goback = True
                    break
                c += 1
                continue

            # place queen
            cords = [j, c]
            placed_queens.append(cords)
            # if last row, append solution and reset all to last unfinished row
            # and last safe column in that row
            if j == k - 1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < k - 1:
                        j = cord[0]
                        c = cord[1]
                for i in range(n - j):
                    placed_queens.pop()
                if j == k - 1 and c == k - 1:
                    placed_queens = []
                    stop = True
                j -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if goback:
            j -= 1
            while j >= 0:
                c = placed_queens[j][1] + 1
                del placed_queens[j]  # delete previous queen coordinates
                if c < k:
                    break
                j -= 1
            if j < 0:
                break
            continue
        j += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
