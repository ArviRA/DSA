class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
    
    def travel(self):
        n = self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n = n.next
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_middle(self,data,pos):
        if self.head is None:
            self.head = Node(data)
            return
        
        n = self.head
        while n.next is not None:
            if n.data  == pos:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next
        print("Position not found")
            
LL = Linked_list()
LL.insert(23)
LL.insert(44)
LL.insert_begin(77)
LL.travel()
print("\n")
LL.insert_middle(100,44)
LL.travel()