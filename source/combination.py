#! python


def combination(n, m):
    """combination(n, m) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n and m is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int) or m < 0 or m > n or not isinstance(m, int):
        raise ValueError('combination is undefined for n = {} and m = {}'.format(n, m))
    # implement combination_recursive below, then
    # call your implementation to verify it passes all tests
    return combination_recursive(n, m)


def combination_recursive(n, m):
    # TODO: implement combination recursively here
    # check if m is one of the base cases
    if m > n/2:
        m = n - m
    else:
        m = m
    if m == 0:
        return 1
    elif m == 1:
        return n
    # check if m is an integer larger than the base cases
    elif m > 1:
        # call function recursively
        return round(n/m * combination_recursive(n - 1, m - 1))


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        n = int(args[0])
        m = int(args[1])
        result = combination(n, m)
        print('C({}, {}) => {}'.format(n, m, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
