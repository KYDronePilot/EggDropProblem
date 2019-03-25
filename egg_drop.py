"""
Solution written by Michael Galliers for the egg drop dynamic programming problem.

"""


def naive_recursive(k, n):
    """
    Naive approach to solving the egg drop problem recursively.

    Args:
        k (int): The number of eggs remaining.
        n (int): The number of floors remaining.

    Returns:
        int: The minimum number of attempts that must be made to find the correct floor.

    """
    # If no floors remaining, no more attempts need to be made.
    if n == 0:
        return 0
    # It will take n attempts to find the correct floor if there is only one egg remaining.
    if k == 1:
        return n
    # Solve the problem recursively.
    return min((max(naive_recursive(k, n - x), naive_recursive(k - 1, x - 1)) + 1 for x in range(1, n + 1)))


def dynamic_iteration(k, n):
    """
    Dynamic, iterative approach to solving the egg drop problem.

    Args:
        k (int): The number of eggs remaining.
        n (int): The number of floors remaining.

    Returns:
        int: The minimum number of attempts that must be made to find the correct floor.

    """
    # If only one egg remains, n attempts must be made to find the correct floor.
    if k == 1:
        return n
    # Lookup table for previous solutions.
    W = [[0 for y in range(n + 1)] for x in range(k)]
    # Initialize the first row.
    for i in range(n + 1):
        W[0][i] = i
    # Start on second row, working downward.
    for i in range(1, k):
        # Calculate values for each cell.
        for j in range(1, n + 1):
            W[i][j] = min((max(W[i][j - x], W[i - 1][x - 1]) for x in range(1, j + 1))) + 1
    # Return the result.
    return W[k - 1][n]


if __name__ == '__main__':
    # Results should be 2, 3, and 4, respectively.
    print(dynamic_iteration(1, 2))
    print(dynamic_iteration(2, 6))
    print(dynamic_iteration(3, 14))
