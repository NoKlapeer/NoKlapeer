import random

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_last(self, value):
        new_item = Item(value)
        if self.head is None:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
        self.length += 1

    def __len__(self):
        return self.length

    def __str__(self):
        current = self.head
        value_str = ""
        while current:
            value_str += str(current.value) + " "
            current = current.next
        return value_str

class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    list = LinkedList()
    for _ in range(10):
        list.add_last(random.randint(1,100))
    list.add_last(20)
    print(list)
    print(len(list))