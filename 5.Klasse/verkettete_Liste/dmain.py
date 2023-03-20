import random


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
    
    def delete(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        
        curr_node = self.head
        while curr_node is not None and curr_node.data != data:
            curr_node = curr_node.next
        
        if curr_node is None:
            return
        
        curr_node.prev.next = curr_node.next
        if curr_node.next is not None:
            curr_node.next.prev = curr_node.prev
    
    def print_list(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data, end=' ')
            temp_node = temp_node.next
        print()

    def __len__(self):
        curr_node = self.head
        length = 0
        while curr_node is not None:
            length += 1
            curr_node = curr_node.next
        return length

if __name__ == "__main__":
    mlist = DoubleLinkedList()
    for _ in range(10):
        mlist.append(random.randint(1,100))
    mlist.append(20)
    mlist.print_list()
    print("Laenge der Liste:", len(mlist))