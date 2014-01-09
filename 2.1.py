# Write code to remove duplicates from an unsorted linked list

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, item):
        current = self.head.next
        while current.next != self.head:
            current = current.next
        list_element = ListElement(item, self.head)
        current.next = list_element

    def size(self):
        suma = 0
        current = self.head.next
        while current != self.head:
            suma += 1
            current = current.next
        return suma 

    def remove_duplicates(self):
        d = {}
        current = self.head
        while current != None:
            d[current.data] = 1
            current = current.next
        no_dup = LinkedList()
        current = self.head
        while current != None:
            if current.data in d:
                no_dup.append(current.data)
                current.remove(current.data)
        return no_dup

   def remove_duplicates2(self):
        d = set()
        current = self.head
        while current != None:
            d.add(current.data)
            current = current.next
        no_dup = LinkedList()
        current = self.head
        while current != None:
            if current.data in d:
                no_dup.append(current.data)
                current.remove(current.data)
        return no_dup









