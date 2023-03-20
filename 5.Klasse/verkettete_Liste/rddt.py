class ArrayList:
        def __init__(self):
            self.platz = 10
            self.len = 0
            self.data = [None] * self.platz

        def add(self, value):
            self.data = self.addtolist(self.data, value)

        def length(self):
            return self.getlength(self.data)

        def print_all(self):
            self.printelements(self.data)

        def addtolist(self, lst, value):
            new_list = []
            for element in lst:
                new_list.append(element)
            new_list.append(value)
            #return new_list
            if self.len == self.platz:
                neuer_platz = self.platz * 2
                neue_data = [None] * neuer_platz
                for i in range(lst):
                    lst.append(element)
                self.data = neue_data
                self.platz = neuer_platz

        def getlength(self, lst):
            count = 0
            for element in lst:
                count += 1
            return count

        def printelements(self, lst):
            for element in lst:
                print(element)