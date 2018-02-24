#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    """time complexity"""
    """Best case: O(1) - find item in the first index"""
    """Worst case: O(n) - find item in the last index or no item in the array"""
    """space complexity"""
    """Best and worst case: O(1) - does not create anything"""
    for index, value in enumerate(array):  # O(n) time
        if item == value:
            return index  # found # O(1) space
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    """time complexity"""
    """Best case: O(1) - find item in the first index"""
    """Worst case: O(n) - find item in the last index or no item in the array"""
    """space complexity"""
    """Best case: O(1) - does not create anything"""
    """Worst case: O(n) - call function n times"""
    if index < len(array):
        value = array[index]
        if item == value:
            return index
        else:
            index += 1
            return linear_search_recursive(array, item, index)  # O(n) time/space
    else:
        return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    """time complexity"""
    """Best case: O(1) - find item in the middle index"""
    """Worst case: O(log2 n) - find item in the last index or no item in the array"""
    """space complexity"""
    """Best case: O(1) - does not create anything"""
    left = 0
    right = len(array) - 1
    while right >= left:
        middle_index = int((left + right)/2)
        value = array[middle_index]
        if item == value:
            return middle_index
        else:
            if item > value:
                left = middle_index + 1
            else:
                right = middle_index - 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    """time complexity"""
    """Best case: O(1) - find item in the middle index"""
    """Worst case: O(log2 n) - find item in the last index or no item in the array"""
    """space complexity"""
    """Best case: O(1) - does not create anything"""
    """Worst case: O(log2 n) - call function (log2 n) times"""
    if left is None and right is None:
        left = 0
        right = len(array) - 1
    else:
        if left > right:
            return None
    middle_index = int((left + right)/2)
    value = array[middle_index]
    if item == value:
        return middle_index
    else:
        if item > value:
            return binary_search_recursive(array, item, middle_index + 1, right)
        else:
            return binary_search_recursive(array, item, left, middle_index - 1)
