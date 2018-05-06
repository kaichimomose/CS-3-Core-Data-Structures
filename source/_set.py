#!python


class Set(object):

    def __init__(self, elements=None):
        """Initialize this set and add the given elements."""
        self.list = list()
        self.size = 0
        if elements is not None:
            for element in elements:
                self.add(element)
                self.size += 1

    def contains(self, element):
        """Return True if this set contains the given element.
        Best case running time: O(1) - first element in the list
        Worst case running time: O(n) for n elements in the set
         - last element"""
        return element in self.list

    def add(self, element):
        """Insert the given item.
        or raise ValueError if the element already exists.
        Running time: O(1) - add item"""
        # Checks element already exists in the set
        if self.contains(element):
            # if so raise error
            raise ValueError("This set has this element.")
        else:
            self.list.append(element)
            self.size += 1

    def remove(self, element):
        """Remove the element,
        or raise ValueError if this queue is empty.
        Running time: O(n) – """
        # Checks element already exists in the set
        if not self.contains(element):
            # if so raise error
            raise ValueError("This set does not have this element.")
        else:
            self.list.remove(element)
            self.size -= 1

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        # Creates new set
        new_set = Set(self.list)
        # Checks element already exists in the new set
        for element in other_set.list:
            if not new_set.contains(element):
                new_set.add(element)
        return new_set

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""
        # Creates new set
        new_set = Set()
        # Checks elements in other set exists in this set
        for element in other_set.list:
            if self.contains(element):
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""
        # Creates new set
        new_set = Set(self.list)
        # Checks elements in other set exists in this set
        for element in other_set.list:
            if not new_set.contains(element):
                new_set.add(element)
            else:
                new_set.remove(element)
        return new_set

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set"""
        # Checks elements in other set exists in this set
        for element in other_set.list:
            if not self.contains(element):
                return False
        return True
