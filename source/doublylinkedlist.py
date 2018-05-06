#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) index is first or last index
        Worst case running time: O(n) index is middle index"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return its data
        if index <= int(self.size/2):
            # count node index
            node_index = 0
            # start at the head node
            node = self.head
            # data
            data = node.data
            while node_index < index:
                # increment node count
                node_index += 1
                # skip to the next node
                node = node.next
                # data
                data = node.data
        else:
            # count down node index
            node_index = self.size - 1
            # start at the head node
            node = self.tail
            # data
            data = node.data
            while node_index > index:
                # increment node count
                node_index -= 1
                # skip to the previous node
                node = node.previous
                # data
                data = node.data
        # data contains the item at the given index
        return data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) index is first or last index
        Worst case running time: O(n) index is middle index"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it

        # create new node with the given item
        new_node = Node(item)

        # increment number of nodes
        self.size += 1

        # base case linked list does not have node
        if self.is_empty():
            # set new node as head
            self.head = new_node
            # set new node as tail
            self.tail = new_node

        # insert at the first index
        elif index == 0:
            # get current head node
            head_node = self.head
            # current head node is front of new node
            new_node.next = head_node
            # point new node as previous node
            head_node.previous = new_node
            # set new node as head
            self.head = new_node

        # insert at the last index
        elif index == self.size - 1:
            # current tail node
            tail_node = self.tail
            # current tail node is behind new node
            tail_node.next = new_node
            # point the tail node as previous node
            new_node.previous = tail_node
            # set new node as tail
            self.tail = new_node

        # insert at the middle
        elif index <= int(self.size/2):
            # count node index
            node_index = 0
            # start from head node
            current_node = self.head
            # node next to current node
            next_node = current_node.next
            # iterate nutil find the node before the given index
            while node_index < index:
                if index == node_index - 1:
                    # set next node after new node
                    new_node.next = next_node
                    # set next node after new node
                    new_node.previous = current_node
                    # set new node after current node
                    current_node.next = new_node
                    # set new node after current node
                    next_node.previous = new_node
                    return
                else:
                    # increment node index
                    node_index += 1
        else:
            # count down node index
            node_index = self.size - 1
            # start from tail node
            current_node = self.tail
            # previous node of current node
            previous_node = current_node.previous
            # iterate nutil find the node before the given index
            while node_index >= index:
                if index == node_index:
                    # set next node after new node
                    new_node.next = current_node
                    # set next node after new node
                    new_node.previous = previous_node
                    # set new node after current node
                    current_node.previous = new_node
                    # set next node after new node
                    previous_node.next = new_node
                    return
                else:
                    # increment node index
                    node_index -= 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) """
        # increment number of nodes
        self.size += 1
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
            # the tial node is previous node of new node
            new_node.previous = self.tail
        # Update tail to new node regardless
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) """
        # increment number of nodes
        self.size += 1
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            # new node is previous node of the head node
            self.head.previous = new_node
        # Update head to new node regardless
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node and the tail node
        left_node = self.head  # Constant time to assign a variable reference
        right_node = self.tail  # Constant time to assign a variable reference
        # count up number of index from left
        left = 0  # Constant time to assign a variable reference
        # count down number of index from right
        right = self.size - 1  # Constant time to assign a variable reference
        # Loop nutil left become larger than right
        while left <= right:  # Up to n/2 iterations if we don't exit early
            # Check if left node's data satisfies the given quality function
            if quality(left_node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return left_node.data  # Constant time to return data
            elif quality(right_node.data):  # Constant time to call quality function
                return right_node.data  # Constant time to return data
            # Skip to the next node
            left_node = left_node.next  # Constant time to reassign a variable
            # Skip to the previous node
            right_node = right_node.previous  # Constant time to reassign a variable
            # Update counter
            left += 1  # Constant time to reassign a variable
            right -= 1  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) replace item in the first node or the last node
        Worst case running time: O(n) if old item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # TODO: Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object

        # check the tail node data for old item
        tail = self.tail
        if tail.data == old_item:
            tail.data = new_item
        else:
            # start from the head node
            node = self.head
            while node is not None:
                if node.data == old_item:
                    node.data = new_item
                    return
                else:
                    # skip to the next node
                    node = node.next
            # if old_item is not found
            raise ValueError('item: {} is not found in this list'.format(old_item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        deleting_node = None
        # Start at the head node and the tail node
        left_node = self.head  # Constant time to assign a variable reference
        right_node = self.tail  # Constant time to assign a variable reference
        # count up number of index from left
        left = 0  # Constant time to assign a variable reference
        # count down number of index from right
        right = self.size - 1  # Constant time to assign a variable reference
        # Create a flag to track if we have found the given item
        found = False
        # Loop nutil left become larger than right
        while left <= right:  # Up to n/2 iterations if we don't exit early
            # Check if left node's data satisfies the given quality function
            if left_node.data == item:  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                deleting_node = left_node  # Constant time to return data
                found = True
                break
            elif right_node.data == item:  # Constant time to call quality function
                deleting_node = right_node  # Constant time to return data
                found = True
                break
            else:
                # Skip to the next node
                left_node = left_node.next  # Constant time to reassign a variable
                # Skip to the previous node
                right_node = right_node.previous  # Constant time to reassign a variable
                # Update counter
                left += 1  # Constant time to reassign a variable
                right -= 1  # Constant time to reassign a variable

        # Check if we found the given item or we never did and reached the tail
        if found:
            self.size -= 1
            # Check if we found a node in the middle of this linked list
            if deleting_node is not self.head and deleting_node is not self.tail:
                # Update the previous node to skip around the found node
                deleting_node.previous.next = deleting_node.next
                # Update the next node to skip around the found node
                deleting_node.next.previous = deleting_node.previous
                # Unlink the found node from its next node
                deleting_node.next = None
                # Unlink the found node from its next node
                deleting_node.previous = None
            if deleting_node is self.head and deleting_node is self.tail:
                self.head = None
                self.tail = None
            # Check if we found a node at the head
            if deleting_node is self.head:
                # Update head to the next node
                self.head = deleting_node.next
                # Unlink the found node from the next node
                deleting_node.next = None
            # Check if we found a node at the tail
            if deleting_node is self.tail:
                # Check if there is a node before the found node
                if deleting_node.previous is not None:
                    # Unlink the previous node from the found node
                    deleting_node.previous.next = None
                # Update tail to the previous node regardless
                self.tail = deleting_node.previous
                # Unlink the found node from the next node
                deleting_node.previous = None
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_doubly_linked_list():
    dll = DoublyLinkedList()
    print(dll)

    print('Appending items:')
    dll.append('A')
    print(dll)
    dll.append('B')
    print(dll)
    dll.append('C')
    print(dll)
    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('size: {}'.format(dll.size))
    print('length: {}'.format(dll.length()))

    print('Getting items by index:')
    for index in range(dll.size):
        item = dll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    dll.delete('B')
    print(dll)
    dll.delete('C')
    print(dll)
    dll.delete('A')
    print(dll)
    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('size: {}'.format(dll.size))
    print('length: {}'.format(dll.length()))


if __name__ == '__main__':
    test_doubly_linked_list()
