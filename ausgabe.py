
class ProzessAusgabe(object):
    def __init__(self, a, m, t):
        self.ausgabeAnzahl = a
        self.ausgabeMenge = m
        self.ausgabeTyp = t

    def getAusgabeAnzahl(self):
        return self.ausgabeAnzahl

    def setAusgabeAnzahl(self, a):
        self.ausgabeAnzahl = a

    def getAusgabeMenge(self):
        return self.ausgabeMenge

    def setAusgabeMenge(self, m):
        self.ausgabeMenge = m

    def getAusgabeTyp(self):
        return self.ausgabeTyp

    def setAusgabeTyp(self, t):
        self.ausgabeTyp = t
