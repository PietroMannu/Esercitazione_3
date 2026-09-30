from studente import Studente
from scuola import Scuola

def avvia_console():
    scuola = Scuola("Istituto Tecnico")
    
    # Dati di prova iniziali
    scuola.aggiungi_studente(Studente("Mario", "Rossi", 15, "Roma"))
    scuola.aggiungi_studente(Studente("Luigi", "Verdi", 18, "Milano"))

    while True:
        print("\n=== GESTIONALE SCUOLA ===")
        print("1. Aggiungi studente")
        print("2. Ricerca studenti piu anziani")
        print("3. Ricerca per eta")
        print("4. Cura studenti (aggiorna citta)")
        print("5. Mostra tutti gli studenti")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            eta = int(input("Eta: "))
            citta = input("Citta: ")
            scuola.aggiungi_studente(Studente(nome, cognome, eta, citta))
            print("[+] Studente aggiunto con successo.")

        elif scelta == "2":
            anziani = scuola.ricerca_anziani()
            print("\n--- Studenti piu anziani ---")
            for s in anziani:
                print(s)

        elif scelta == "3":
            eta_cercata = int(input("Inserisci l'eta da cercare: "))
            risultati = scuola.ricerca_per_eta(eta_cercata)
            print(f"\n--- Studenti con {eta_cercata} anni ---")
            for s in risultati:
                print(s)

        elif scelta == "4":
            cognome = input("Cognome dello studente da aggiornare: ")
            nuova_citta = input("Nuova citta di residenza: ")
            if scuola.cura_studenti(cognome, nuova_citta):
                print("[+] Citta aggiornata con successo!")
            else:
                print("[-] Nessun studente trovato con questo cognome.")

        elif scelta == "5":
            print("\n--- Elenco Studenti ---")
            for s in scuola.studenti:
                print(s)

        elif scelta == "0":
            print("Uscita dal programma.")
            break

if __name__ == "__main__":
    avvia_console()