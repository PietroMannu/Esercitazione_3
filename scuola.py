from studente import Studente

class Scuola:
    def __init__(self, nome: str):
        self.nome = nome
        self.studenti = []

    def aggiungi_studente(self, studente: Studente):
        self.studenti.append(studente)

    def ricerca_anziani(self) -> list:
        if not self.studenti:
            return []
        max_eta = max(s.eta for s in self.studenti)
        return [s for s in self.studenti if s.eta == max_eta]

    def ricerca_per_eta(self, eta: int) -> list:
        return [s for s in self.studenti if s.eta == eta]

    def cura_studenti(self, cognome: str, nuova_citta: str) -> bool:
        trovato = False
        for s in self.studenti:
            if s.cognome.lower() == cognome.lower():
                s.citta = nuova_citta
                trovato = True
        return trovato