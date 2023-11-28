#!/usr/bin/python3
"""CHESS Thing!"""


import sys


def print_solution(board):
    """
    print_solution prints each queen's position in a solution.
    It iterates over the list of queens and prints each pair of [row, column].
    """
    for queen in board:
        print(queen, end=' ')
    print()


def is_safe(queens, column):
    """
    is_safe function checks if it's safe to place a queen in the given column.
    It ensures that no queens are in the same column or diagonals
    """
    for queen in queens:
        if queen[1] == column or \
           abs(queen[0] - len(queens)) == abs(queen[1] - column):
            return False
    return True


def solve_nqueens(n):
    """
    solve_nqueens function initializes an empty list to store solutions
    and calls the solve function to find solutions.

    solve function recursively explores possible queen placements
    and adds valid solutions to the list.
    """
    solutions = []
    solve([], n, solutions)
    return solutions


def solve(queens, n, solutions):
    """
    solve function recursively explores possible queen placements
    and adds valid solutions to the list.
    """
    if len(queens) == n:
        solutions.append(queens[:])
        return

    for i in range(n):
        if is_safe(queens, i):
            queens.append([len(queens), i])
            solve(queens, n, solutions)
            queens.pop()


def nqueens(n):
    """
    The nqueens function is responsible for handling the input,
    checking its validity
    and calling the solve_nqueens function to obtain a list of solutions.

    It then iterates over the list of solutions
    and prints each solution using the print_solution function.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = solve_nqueens(n)
    for solution in board:
        print_solution(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
