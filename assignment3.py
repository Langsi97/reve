def generate_sequence(n):
    # Taking care of the infinite recursion in case n == 0.
    if n == 0:
        raise RecursionError('maximum recursion depth exceeded')
    # Base case: if n is already 1, return a list with just 1.
    elif n == 1:
        return [1]
    # If n is even, add it to the list and recursively call the function with n/2.
    elif n % 2 == 0:
        return [n] + generate_sequence(n // 2)
    # If n is odd, add it to the list and recursively call the function with 3n+1.
    else:
        return [n] + generate_sequence(3 * n + 1)

    "------------------------------"


def compute_power(n: int, m: int) -> int:
    """
    Computes the result of raising n to the power of m (i.e. n^m)
    in an efficient way using recursion.

    """
    if m == 0:
        # If m is 0, base case: any number raised to 0 is 1
        return 1
    elif m == 1:
        # If m is 1, base case: any number raised to 1 is itself
        return n
    elif m % 2 == 0:
        # If m is even, use the property n^(m/2) * n^(m/2) = n^m
        # compute n^(m/2) and multiply the result with itself in a recursion mode.
        return compute_power(n, m//2) * compute_power(n, m//2)
    else:
        # If m is odd, use the property n^m = n * n^(m-1)
        # compute n^(m-1) and multiply the result with n in a recursion mode.
        return n * compute_power(n, m-1)
