def contains(text, pattern):
    # iteratively
    # text = text.lower()
    # for i in range(len(text) - len(pattern) + 1):
    #     slice = text[i:i+len(pattern)]
    #     if slice == pattern:
    #         return True
    # return False

    # recursively
    text = text.lower()
    if len(text) < len(pattern):
        return False
    elif text[:len(pattern)] == pattern:
        return True
    else:
        return contains(text[1:], pattern)


def find_index(text, pattern, index=0):
    # iteratively
    # text = text.lower()
    # for i in range(len(text) - len(pattern) + 1):
    #     slice = text[i:i+len(pattern)]
    #     if slice == pattern:
    #         return i
    # return None

    # recursively
    text = text.lower()
    if len(text[index:]) < len(pattern):
        return None
    elif text[index:index+len(pattern)] == pattern:
        return index
    else:
        index += 1
        return find_index(text, pattern, index)


def find_all_indexes(text, pattern, index=0, indexes=[]):
    # iteratively
    # text = text.lower()
    # indexes = []
    # range_ = len(text) - len(pattern) + 1
    # if pattern == '':
    #     range_ = len(text) - len(pattern)
    # for i in range(range_):
    #     slice = text[i:i+len(pattern)]
    #     if slice == pattern:
    #         indexes.append(i)
    # return indexes

    # recursively
    if index == 0:
        indexes = []
    text = text.lower()
    if len(text[index:]) < len(pattern):
        return indexes
    elif text[index:] == '':
        return indexes
    else:
        if text[index:index+len(pattern)] == pattern:
            indexes.append(index)
        index += 1
        return find_all_indexes(text, pattern, index, indexes)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
