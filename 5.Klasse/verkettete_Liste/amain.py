import random

class ArrayList:
    def __init__(self):
        self.platz = 10
        self.len = 0
        self.data = [None] * self.platz

    def add(self, element):
        self.mache_platz()
        self.data[self.len] = element
        self.len += 1

    def remove(self, index):
        for i in range(index, self.len-1):
            self.data[i] = self.data[i+1]
        self.data[self.len-1] = None
        self.len -= 1

    def __getitem__(self, index):
        return self.data[index]

    def length(self):
        return self.len

    def mache_platz(self):
        if self.len == self.platz:
            neuer_platz = self.platz * 2
            neue_data = [None] * neuer_platz
            for i in range(self.len):
                neue_data[i] = self.data[i]
            self.data = neue_data
            self.platz = neuer_platz

    def __str__(self):
        return str(self.data[:self.len])

if __name__ == "__main__":
    arraylist = ArrayList()
    for i in range(10):
        arraylist.add(random.randint(1, 100))
    print("Länge von Arraylist:", arraylist.length())
    print("Liste ausgeben:", arraylist)
    such_index = int(input("Gib einen Index zum Finden der Zahl ein: "))
    print("Index von", such_index, "ist", arraylist[such_index])
    entf_index = int(input("Welcher Index soll gelöscht werden? "))
    arraylist.remove(entf_index)
    print("Liste ausgeben:", arraylist)

    