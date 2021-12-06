
class EinsatzstoffeEingabe(object):
    def __init__(self, m, t, q):
        self.menge = m
        self.typ = t
        self.quelle = q

    def getMenge(self):
        return self.menge

    def setMenge(self, m):
        self.menge = m

    def getTyp(self):
        return self.typ

    def setTyp(self, t):
        self.typ = t

    def getQuelle(self):
        return self.quelle

    def setQuelle(self, q):
        self.quelle = q