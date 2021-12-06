
class StahlVerarbeitung(object):
    def __init__(self, a, n, d):
        self.schrittenAnzahl = a
        self.schrittName = n
        self.schrittDauer = d

    def getAnzahl(self):
        return self.schrittenAnzahl

    def setAnzahl(self, a):
        self.schrittenAnzahl = a

    def getSchrittName(self):
        return self.schrittName

    def setSchrittName(self, n):
        self.schrittName = n

    def getSchrittDauer(self):
        return self.schrittDauer

    def setSchrittDauer(self, d):
        self.schrittDauer = d


class HauptVerarbeitung(StahlVerarbeitung):
    def __init__(self, a, n, d, pa):
        self.stahlProzessAusgabe = pa
        super().__init__(a, n, d)

    def getAnzahl(self):
        return self.schrittenAnzahl

    def setAnzahl(self, a):
        self.schrittenAnzahl = a

    def getSchrittName(self):
        return self.schrittName

    def setSchrittName(self, n):
        self.schrittName = n

    def getSchrittDauer(self):
        return self.schrittDauer

    def setSchrittDauer(self, d):
        self.schrittDauer = d

    def getStahlProzessAusgabe(self):
        return self.stahlProzessAusgabe

    def setStahlProzessAusgabe(self, pa):
        self.stahlProzessAusgabe = pa


class VorVerarbeitung(StahlVerarbeitung):
    def __init__(self, a, n, d, es):
        self.stahlEinsatzstoffeEingabe = es
        super().__init__(a, n, d)

    def getAnzahl(self):
        return self.schrittenAnzahl

    def setAnzahl(self, a):
        self.schrittenAnzahl = a

    def getSchrittName(self):
        return self.schrittName

    def setSchrittName(self, n):
        self.schrittName = n

    def getSchrittDauer(self):
        return self.schrittDauer

    def setSchrittDauer(self, d):
        self.schrittDauer = d

    def getStahlEinsatzstoffeEingabe(self):
        return self.stahlEinsatzstoffeEingabe

    def setStahlEinsatzstoffeEingabe(self, es):
        self.stahlEinsatzstoffeEingabe = es
