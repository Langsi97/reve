"""The function f performs a recursive operation on the input number x. 
It checks if x is even or odd, and if it is even, it adds 1 to the result of 
recursively calling the function on x divided by 2. If it is odd, it simply returns 0.

Here are the expected outputs for the given inputs:

f(2): 2 is even, so f(2) will add 1 to the result of f(1). Since 1 is odd, f(1)
 will return 0. Therefore, f(2) will return 1.
f(3): 3 is odd, so f(3) will simply return 0.
f(4): 4 is even, so f(4) will add 1 to the result of f(2). We already know that
f(2) is 1, so f(4) will return 2.
f(2100): 2100 is a very large even number, so f(2100) will add 1 to the result
 of f(299), which in turn will add 1 to the result of f(298), and so on, until 
 it reaches f(2), which is 1. Therefore, f(2100) will return 101.
f((2**100)*(3 **100)): This number is neither even nor odd, so the function 
will not terminate and will instead go into an infinite loop, causing a stack 
overflow error.
Note that the function f is designed to count the number of times an even 
number can be divided by 2 before it becomes odd. Therefore, the output for 
any even input will be the number of times it can be divided by 2 
 becoming odd, plus 1. The output for any odd input will always be 0."""
#-----------------------------------------------#


import math


def max_index_list(L):
    if len(L) == 1:
        return 0
    else:
        max_index = max_index_list(L[1:])
        if L[0] > L[max_index]:
            return 0
        else:
            return max_index + 1
# --------------------------


def min_list(L, i, j):
    if i == j:
        return L[i]
    mid = (i + j) // 2
    left_min = min_list(L, i, mid)
    right_min = min_list(L, mid+1, j)
    return min(left_min, right_min)
# ----------------------


def count_different_elements(L, seen=set()):
    count = 0
    for elem in L:
        if isinstance(elem, (int, float, str)):
            if elem not in seen:
                seen.add(elem)
                count += 1
        elif isinstance(elem, list):
            count += count_different_elements(elem, seen)
    return count
# -------------------------


def mybit(n):
    if n == 1:
        print("0")
        print("1")
    else:
        mybit(n-1)
        for i in range(2**(n-1), 2**n):
            binary_str = format(i, "0" + str(n) + "b")
            print(binary_str)
# --------------


def knight_tour(n, path, visited):
    """
    Recursive function to solve the knight's tour problem on a 5x5 board.
    n: the current move number (from 0 to 24).
    path: a list containing the current path of moves.
    visited: a set containing the positions already visited by the knight.
    Returns a list of moves that solve the problem, or None if there's no solution.
    """
    if n == 25:
        # Base case: all squares have been visited, return the solution path
        return path

    # Try all possible moves from the current position
    row, col = divmod(path[-1], 5)
    for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1),
                   (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 5 and 0 <= nc < 5 and nr*5 + nc not in visited:
            # Move is valid, make it and continue the search recursively
            visited.add(nr*5 + nc)
            path.append(nr*5 + nc)
            solution = knight_tour(n+1, path, visited)
            if solution is not None:
                # Found a solution, return it
                return solution
            # Solution not found, backtrack and try next move
            visited.remove(nr*5 + nc)
            path.pop()

    # No solution found from this position
    return None
# ---------------------


def binary_search_rec(lst, x):
    # Define the recursive search function
    def search(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return search(low, mid-1)
        else:
            return search(mid+1, high)

    # Call the recursive search function
    return search(0, len(lst)-1)

# ----------------


def jump_search(lst, x):
    jump_length = int(math.sqrt(len(lst)))
    left, right = 0, jump_length

    while right < len(lst) and lst[right] <= x:
        left = right
        right += jump_length

    for i in range(left, min(right, len(lst))):
        if lst[i] == x:
            return i

    return -1
# -------------------


def bucket_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for val in arr:
            buckets[(val // exp) % 10].append(val)
        arr = [val for bucket in buckets for val in bucket]
        exp *= 10
    return arr
