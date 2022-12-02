class Person:
    def __init__(self, name, geschlecht, abteilung):
        self.name = name
        self.geschlecht = geschlecht
        self.abteilung = abteilung

class Abteilung:
    def __init__(self, name, anzMA):
        self.name = name
        self.anzMA = anzMA

class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung, firma):
        super().__init__(name, geschlecht, abteilung)
        self.firma = firma

class Gruppenleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung, firma):
        super().__init__(name, geschlecht, abteilung, firma)

class Firma:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = []
        self.gruppenleiter = []
        self.abteilungen = []
    
    def anz_mitarbeiter(self):
        anzahl = 0
        for i in self.mitarbeiter:
            anzahl+=1
        return anzahl

    def anz_gruppenleiter(self):
        anzahl = 0
        for i in self.gruppenleiter:
            anzahl+=1
        return anzahl

    def anz_abteilungen(self):
        anzahl = 0
        for i in self.abteilungen:
            anzahl+=1
        return anzahl
    
    def mitarbeiterstärke(self):
        anzMAdavor = 0
        groesste = 0
        for i in self.abteilungen:
            if(i.anzMA > anzMAdavor):
                groesste = i.name
                anzMAdavor = i.anzMA
        return groesste
    
    def proz_fraumann(self):
        anzMitA = 0
        for i in self.abteilungen:
            anzMitA += i.anzMA
        mann = 0
        frau = 0
        for j in self.mitarbeiter:
            if(j.geschlecht == "m"):
                mann+=1
            else: frau+=1
        for j in self.gruppenleiter:
            if(j.geschlecht == "m"):
                mann+=1
            else: frau+=1
        return "Maenner:", mann/anzMitA, "Frauen:", frau/anzMitA

wi = Abteilung("Wirtschaft", 1)
mas = Abteilung("Maschinenbau", 2)
firma = Firma("Rast und Ruhr GmbH")
ma1 = Mitarbeiter("Marvin", "m", wi, firma)
ma2 = Mitarbeiter("Ulrike", "w", mas, firma)
gl1 = Gruppenleiter("Roland", "m", mas, firma)

firma.mitarbeiter.append(ma1)
firma.mitarbeiter.append(ma2)
firma.gruppenleiter.append(gl1)

firma.abteilungen.append(wi)
firma.abteilungen.append(mas)

print("Anzahl der Mitarbeiter:", firma.anz_mitarbeiter())
print("Anzahl der Gruppenleiter:",firma.anz_gruppenleiter())
print("Anzahl der Abteilungen:",firma.anz_abteilungen())
print("Abteilung mit groesster Mitarbeiterstärke:", firma.mitarbeiterstärke())
print("Prozentanteil Männer und Frauen:", firma.proz_fraumann())
