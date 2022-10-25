class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class Double:
    def __init__(self) -> None:
        self.head = None

    def travel(self):
        n = self.head
        if n is None:
            print("List is empty")
            return
        while n.next is not None:
            print(n.data,"->")
            n = n.next
    def reverse_travel(self):
        n = self.head
        if n is None:
            print("List is empty")
            return
        while n is not None:
            n = n.next
        while n.prev is not None:
            print(n.data)
            n = n.prev

dl = Double()
dl.travel()