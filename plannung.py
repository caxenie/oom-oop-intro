import random

MIN_EBENE = 1.4
MAX_EBENE = 2.5

class StahlProzessPlannung(object):
    def __init__(self, a, n, g):
        self.prozessGliederAnzahl = a
        self.prozessGliederName = n
        self.prozessGlieder = g

    def getProzessGliederAnzahl(self):
        return self.prozessGliederAnzahl

    def setProzessGliederAnzahl(self, a):
        self.prozessGliederAnzahl = a

    def getProzessGliederName(self):
        return self.prozessGliederName

    def setProzessGliederName(self, n):
        self.prozessGliederName = n

    def getProzessGlieder(self):
        return self.prozessGlieder

    def setProzessGlieder(self, g):
        self.prozessGlieder = g

    def getGliederDauer(self, name):
        gDauer = 0
        for i in range(self.prozessGliederAnzahl):
            if self.prozessGliederName == name:
                gDauer = self.prozessGlieder[i].dauer()
        return gDauer

    def getGesamtGliederDauer(self):
        sumDauer=0
        for i in range(self.prozessGliederAnzahl):
            sumDauer += self.prozessGlieder[i].dauer()
        return sumDauer

    def optimizeProzessDauer(self):
        if self.getGesamtGliederDauer() < MIN_EBENE:
            for i in range(self.prozessGliederAnzahl):
                self.prozessGlieder[i].setDauer(MIN_EBENE)
        elif self.getGesamtGliederDauer() > MAX_EBENE:
            for i in range(self.prozessGliederAnzahl):
                self.prozessGlieder[i].setDauer(self.prozessGlieder[i].getDauer() + self.getGesamtGliederDauer() / 5.0)
        else:
            for i in range(self.prozessGliederAnzahl):
                self.prozessGlieder[i].setDauer(
                    self.prozessGlieder[i].getDauer() + self.getGesamtGliederDauer() / 5.0 + random.random())