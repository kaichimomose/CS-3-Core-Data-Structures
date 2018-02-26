#!python


def permutation(n, m):
    """permutation(n, m) returns the product of the integers (n - m + 1) through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n or m < 0 or non-integer m"""
    # check if n and m is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int) or m < 0 or m > n or not isinstance(m, int):
        raise ValueError('permutation is undefined for n = {} and m = {}'.format(n, m))
    # implement permutation_recursive below, then
    # call your implementation to verify it passes all tests
    return permutation_recursive(n, m)


def permutation_recursive(n, m):
    # TODO: implement permutation recursively here
    # check if n is one of the base cases
    if m == 0:
        return 1
    elif m == 1:
        return n
    # check if m is an integer larger than the base cases
    elif m > 1:
        # call function recursively
        return n * permutation_recursive(n - 1, m - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        n = int(args[0])
        m = int(args[1])
        result = permutation(n, m)
        print('P({}, {}) => {}'.format(n, m, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
