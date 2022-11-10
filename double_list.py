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
        #print("Normal traversal")
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
    def add_after(self,data,x):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            
            while n is not None:
                if x==n.data:
                    break
                n = n.next
            if n is None:
                print(x,"not found")
                return
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node
    def add_before(self,data,x):
         if self.head is None:
            print("List is empty")
         else:
            n = self.head 
            while n is not None:
                if x==n.data:
                    break
                n = n.next
            if n is None:
                print(x,"not found")
                return
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.head = new_node
                n.prev = new_node
    def delete_begin(self):
        if self.head == None:
            print("List is empty")
            return
        if self.head.next == None:
            self.head = None
            print("Head deleted list is empty now")
            return
        self.head = self.head.next
        self.head.prev = None
    def delete_end(self):
        if self.head == None:
            print("List is empty")
            return
        if  self.head.next == None:
                self.head = None
                print("Last node is  deleted list is empty now")
                return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
    def delete_value(self,x):
        if self.head == None:
            print("List is empty")
            return
        if self.head.next == None:
            if self.head.data == x:
                self.head = None
                print("Head deleted list is empty now")
                return
        if self.head.data == x:
                self.head = self.head.next
                self.head.prev = None
                return
        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
            return
        else:
            if n.data == x:
                n.prev.next = None
                return
        print(x,"vaue is not present")
        
        
        
        
        

        

    




                







dl = Double()
dl.add_begin(10)
dl.add_begin(20)
dl.add_end(30)
dl.add_end(40)
#dl.add_before(100,88)
dl.add_after(99,40)
dl.travel()
print("\n")
#dl.delete_begin()
dl.delete_end()
dl.delete_value(30)
dl.travel()
#dl.reverse_travel()