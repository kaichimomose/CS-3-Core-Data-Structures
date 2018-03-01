#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # iteratively
    lowercase_text = text.lower()
    if pattern != "":
        # counts pattern index
        pattern_index = 0
        text_index = 0
        while text_index < len(text):
            # checks rest of text length and pattern length
            if pattern_index == 0 and len(text) - text_index < len(pattern):
                # if no match with pattern and rest of text length is shoter than
                # pattern length, it is false
                return False
            else:
                # checks each character in text
                if lowercase_text[text_index] == pattern[pattern_index]:
                    if pattern_index == len(pattern)-1:
                        return True
                    else:
                        # increments text_index
                        text_index += 1
                        # increments pattern_index
                        pattern_index += 1
                else:

                    text_index = text_index - pattern_index + 1
                    # resets pattern_index
                    pattern_index = 0
        # defalt false
        return False
    else:
        return True


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    # iteratively
    lowercase_text = text.lower()
    # starting index of the first occurrence of pattern in text
    starting_index = None
    if pattern != "":
        # counts pattern index
        pattern_index = 0
        text_index = 0
        while text_index < len(text):
            # checks rest of text length and pattern length
            if pattern_index == 0 and len(text) - text_index < len(pattern):
                # if no match with pattern and rest of text length is shoter than
                # pattern length, it is false
                return starting_index
            else:
                # checks each character in text
                if lowercase_text[text_index] == pattern[pattern_index]:
                    if starting_index is None:
                        starting_index = text_index
                    if pattern_index == len(pattern)-1:
                        return starting_index
                    else:
                        # increments text_index
                        text_index += 1
                        # increments pattern_index
                        pattern_index += 1
                else:

                    text_index = text_index - pattern_index + 1
                    # resets pattern_index
                    starting_index = None
                    pattern_index = 0
        # defalt false
        return starting_index
    else:
        return 0



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    # iteratively
    lowercase_text = text.lower()
    # starting index of the first occurrence of pattern in text
    starting_index = None
    # starting indexes of the first occurrence of pattern in text
    starting_indexes = []
    # counts pattern index
    pattern_index = 0
    text_index = 0
    while text_index < len(text):
        if pattern == "":
            starting_indexes.append(text_index)
            text_index += 1
        else:
            # checks rest of text length and pattern length
            if pattern_index == 0 and len(text) - text_index < len(pattern):
                # if no match with pattern and rest of text length is shoter than
                # pattern length, it is false
                return starting_indexes
            else:
                # checks each character in text
                if lowercase_text[text_index] == pattern[pattern_index]:
                    if starting_index is None:
                        starting_index = text_index
                    if pattern_index == len(pattern)-1:
                        # save starting_index in list
                        starting_indexes.append(starting_index)
                        # resets pattern_index
                        text_index = text_index - pattern_index + 1
                        starting_index = None
                        pattern_index = 0
                    else:
                        # increments text_index
                        text_index += 1
                        # increments pattern_index
                        pattern_index += 1
                else:

                    text_index = text_index - pattern_index + 1
                    # resets pattern_index
                    starting_index = None
                    pattern_index = 0

    # defalt false
    return starting_indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # # TODO: Uncomment these lines after you implement find_all_indexes
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
