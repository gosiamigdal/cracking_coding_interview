# Given a circular linked list, implement an algorithm which returns node 
# at the beginning of the loop


class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Circular_list():
    def __init__(self):
        self.head = Node(None, None)
        self.head.next = self.head

    def return_beginning_node(self):
        d = {}
        current = self.head
        while current != None:
            if current in d:
                return current
            else:
                d[current] = 1
            current = current.next
        return None 


    def return_beginning_node2(self):
        current = self.head
        if current == None:
            return current
        current2 = current.next
        while current != current2:
            if current2 == None or current2.next == None:
                return None
            current = current.next
            current2 = current2.next.next
        return current
