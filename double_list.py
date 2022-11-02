from tkinter import N


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class Double:
    def __init__(self) -> None:
        self.head = None

    def travel(self):
        print("Normal traversal")
        n = self.head
        if n is None:
            print("List is empty")
            return
        while n is not None:
            print(n.data,"->",end=" ")
            n = n.next
    def reverse_travel(self):
        print("\nReverse traversal")
        n = self.head
        if n is None:
            print("List is empty")
            return
        while n.next is not None:
            n = n.next
        while n is not None:
            print(n.data,"->",end= " ")
            n = n.prev
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        #print("Done")
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n


dl = Double()
dl.add_begin(10)
dl.add_begin(20)
dl.add_end(30)
dl.add_end(40)
dl.travel()
dl.reverse_travel()