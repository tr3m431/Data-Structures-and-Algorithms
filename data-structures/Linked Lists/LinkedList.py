class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        new_pos = 1

        for elem in range(position - 1):
            if current == None and new_pos == position:
                return None
            else:
                current = current.next
                new_pos += 1

        return current



    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head

        if position == 1:
            old_head = self.head
            self.head = new_element
            current = self.head
            current.next = old_head

        else:
            for elem in range(position - 2):
                current = current.next

            next_elem = current.next
            current.next = new_element
            new_element.next = next_elem

        pass


    def delete(self, value):
        """Delete the first node with a given value."""

        current = self.head
        if current.value == value:
            self.head = current.next
            current.next = None
        else:
            while current.next.value != value:
                current = current.next

            current.next = current.next.next
            current.next.next = None

        pass

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
