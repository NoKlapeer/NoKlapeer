import random

class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def add(self, item):
        self.data.append(item)

    def remove(self, index):
        del self.data[index]

    def __getitem__(self, index):
        return self.data[index]

    def index_of(self, item):
        return self.data.index(item)
    
    def __str__(self):
        return str(self.data)

if __name__ == "__main__":
    arraylist = ArrayList()
    for i in range(10):
        arraylist.add(random.randint(1, 100))
    print("Länge von Arraylist:", arraylist.length())
    print("Liste ausgeben:", arraylist)
    search_value = int(input("Gib eine Zahl zum Finden des Indexes ein: "))
    print("Index von", search_value, "ist", arraylist.index_of(search_value))
    search_index = int(input("Gib einen Index zum Finden der Zahl ein: "))
    print("Index von", search_index, "ist", arraylist[search_index])
    print("Index 2 wird gelöscht ...")
    arraylist.remove(2)
    print("Liste ausgeben:", arraylist)

    