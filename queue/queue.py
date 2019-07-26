class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Stuff to add to list
    def add_to_tail(self, value):
        new_node = Node(value)

        # Before setting new tail, we need to point the previous tail
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:  # We don't have an empty list
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)

        # Before setting new head, we need to point the previous tail
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:  # We don't have an empty list
            new_node.set_next(self.head)
            self.head = new_node

    # Does this list already contain a value?
    def contains(self, value):
        # If no head, the list is emplty, therefore it cannot have our value
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    # Stuff to remove from list
    def remove_from_head(self):
        if self.head:
            removed_head = self.head.get_value()
            if not self.head.next_node:
                self.head = None
                self.tail = None
                return removed_head
            self.head = self.head.next_node
            return removed_head
        else:
            print('else')
            return None

    # Stuff to find in List


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, value):
        # self.storage.append(item)
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # if self.storage:
        #     return self.storage.pop(0)
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        # return len(self.storage)
        return self.size
