#Implement an algorithm to find the nth to last element of a singly linked list


class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linked_list():
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item, None)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node


    def printer(self):
        current = self.head
        while current != None:
            print "Print: ", current.data
            current = current.next

    def find_nth(n):
        find_index = n 
        current = self.head
        current_ind = 0
        result = Linked_list()
        while current_ind != find_index:
            result.append(current)
            current = current.next
            current_ind += 1
        return result




        

        