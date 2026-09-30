class Studente:
    def __init__(self, nome: str, cognome: str, eta: int, citta: str):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta

    def classificazione(self) -> str:
        return "Biennio" if self.eta <= 15 else "Triennio"

    def __str__(self):
        return f"{self.cognome} {self.nome}, {self.eta} anni ({self.citta}) - {self.classificazione()}"