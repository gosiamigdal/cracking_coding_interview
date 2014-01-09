# Implement an algorithm to delete a node in the middle of a single linked list.
# EXAMPLE
# Input: the node ‘c’ from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a->b->d->e

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linked_list():
    def __init__(self):
        self.head = None

    def size(self):
        # czy trzeba sprawdzić czy pusta
        size = 0
        current = self.head
        while current != None:
            size += 1
            current = current.next
        return size 

    def remove_middle(self):
        size = size(self)
        remove_index = size / 2
        previous = self.head 
        current = self.head.next
        current_index = 0
        while current_index != remove_index:
            current_index += 1
            current = current.next
            previous = previous.next
        previous.next = current.next 

        
