#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) for n items in the list
    TODO: Memory usage: O(1)"""
    # Check that all adjacent items are in order, return early if not
    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n*n) for n items in the list
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Repeat until all items are in sorted order
    is_sorted = False
    # while not is_sorted(items):
    while not is_sorted:
        is_sorted = True
        for i in range(len(items) - 1):
            # Swap adjacent items that are out of order
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                is_sorted = False


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n*n)? for n items in the list
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Repeat until all items are in sorted order
    for i in range(len(items) - 1):
        # get first unsorted item
        minimum_item = items[i]
        # track minimum item index
        minimum_item_index = i
        # loop through unsorted items
        for j in range(i+1, len(items)):
            # Find minimum item in unsorted items
            current_item = items[j]
            if minimum_item > current_item:
                minimum_item = current_item
                # update minimum item index
                minimum_item_index = j
        # Swap it with first unsorted item
        items[i], items[minimum_item_index] = items[minimum_item_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n*n)? for n items in the list
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    for i in range(1, len(items)):
        # Take first unsorted item
        inserting_item = items[i]
        # track inserting item index
        inserting_item_index = i
        # loop through sorted items
        for j in range(0, i):
            current_item = items[(i-1) - j]
            if inserting_item < current_item:
                # Insert it in sorted order in front of items
                items[inserting_item_index], items[(i-1) - j] = items[(i-1) - j], items[inserting_item_index]
                # update inserting item index
                inserting_item_index = (i-1) - j


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n + m) for n items in one list and m items in another list
    TODO: Memory usage: O(n + m) for n items in one list and m items in another list"""
    front_index1 = 0
    front_index2 = 0
    sorting_list = []
    # Repeat until one list is empty
    while front_index1 < len(items1) and front_index2 < len(items2):
        # Find minimum item in both lists and append it to new list
        smallest_item1 = items1[front_index1]
        smallest_item2 = items2[front_index2]
        if smallest_item1 < smallest_item2:
            sorting_list.append(smallest_item1)
            front_index1 += 1
        else:
            sorting_list.append(smallest_item2)
            front_index2 += 1
    # Append remaining items in non-empty list to new list
    if front_index1 != len(items1):
        sorting_list.extend(items1[front_index1:])
    else:
        sorting_list.extend(items2[front_index2:])
    return sorting_list

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(m*m) for half of items (m=n/2) in the list
    TODO: Memory usage: O(n) for n items in the list"""
    # Split items list into approximately equal halves
    middle_index = int((len(items))/2)
    left_half = items[0:middle_index]
    right_half = items[middle_index:len(items)]
    # Sort each half using any other sorting algorithm
    selection_sort(left_half)
    selection_sort(right_half)
    # Merge sorted halves into one list in sorted order
    items = merge(left_half, right_half)
    return items

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n * logn)
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    if len(items) == 1:
        return items
    # Split items list into approximately equal halves
    middle_index = int((len(items))/2)
    left_half = items[:middle_index]
    right_half = items[middle_index:]
    # Sort each half by recursively calling merge sort
    items1 = merge_sort(left_half)
    items2 = merge_sort(right_half)
    # Merge sorted halves into one list in sorted order
    items = merge(items1, items2)
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    if sort == merge_sort or sort == split_sort_merge:
        items = sort(items)
    else:
        sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
