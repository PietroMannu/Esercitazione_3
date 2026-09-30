from studente import Studente
from scuola import Scuola

def esegui_test():
    scuola = Scuola("Scuola Test")

    # 1. Test metodi base
    s1 = Studente("Marco", "Rossi", 14, "Roma")
    s2 = Studente("Elena", "Verdi", 17, "Milano")
    
    assert s1.classificazione() == "Biennio"
    assert s2.classificazione() == "Triennio"
    print("[OK] Test classificazione superato.")

    scuola.aggiungi_studente(s1)
    scuola.aggiungi_studente(s2)

    # Test cura studenti (cambio citta)
    scuola.cura_studenti("Rossi", "Napoli")
    assert s1.citta == "Napoli"
    print("[OK] Test cura studenti (cambio citta) superato.")

    # 2. Test caricamento di 1000 studenti
    print("Caricamento 1000 studenti in corso...")
    for i in range(1000):
        scuola.aggiungi_studente(Studente(f"Nome{i}", f"Cognome{i}", 15 + (i % 4), "CittaTest"))

    assert len(scuola.studenti) == 1002
    print(f"[OK] Test 1000 studenti superato! Totale studenti nel sistema: {len(scuola.studenti)}")

if __name__ == "__main__":
    esegui_test()