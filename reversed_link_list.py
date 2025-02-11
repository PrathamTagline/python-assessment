class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkList:
    def __init__(self):
        self.head = None

    def insert_node_in_tail(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            print()
            new_node.next = self.head
            self.head = new_node


    def display(self):
        
        current_node = self.head
        while current_node:
            print(current_node.data,end=" -> ")
            current_node = current_node.next

    def reveserd(self):
        pass

        
        

a = linkList()
a.insert_node_in_tail(21)
a.insert_node_in_tail(22)

print(a.display())