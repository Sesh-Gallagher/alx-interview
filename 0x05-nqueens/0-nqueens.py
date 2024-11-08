#!/usr/bin/python3
"""
Module that represents the solution
to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Represents the backtrack function to find solution
    """
    if r == n:
        res = []
        for a in range(len(board)):
            for b in range(len(board[a])):
                if board[a][b] == 1:
                    res.append([a, b])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Represents the solution to nqueens problem
    Args: n (int): number of queens. Must be >= 4
    Return: List of lists representing coordinates of each
            queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
