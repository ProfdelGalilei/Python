import random
import time

def Intro():
    print('''Dopo un lungo cammino, si erge di fronte a te la montagna dei draghi. 
Tra una folta boscaglia, vedi il sentiero che si biforca e scorgi in lontananza, 
in fondo a ciascun sentiero, una caverna. La leggenda racconta che in una di 
queste caverne si trova un drago pericolosissimo, mentre nell'altra c'è un 
drago buono, che regala monete d'oro dal suo tesoro a tutti i visitatori…''')
    print()
    nome = input('Come ti chiami, coraggioso avventuriero? ')
    print(f'\nBenvenuto {nome}! Preparati per la tua avventura!')
    time.sleep(2)
    return nome

def scegliCav(num_caverne):
    while True:
        print(f'\nIn quale caverna vuoi entrare? (da 1 a {num_caverne})')
        print(f'(Ci sono {num_caverne} caverne tra cui scegliere)')
        caverna = input()
        if caverna.isdigit():
            if 1 <= int(caverna) <= num_caverne:
                return caverna
        print(f"Per favore, inserisci un numero tra 1 e {num_caverne}")

def verifica(CavScelta, nome, num_caverne):
    punteggio = 0
    print('Ti avvicini con cautela alla caverna...')
    time.sleep(2)
    print('Si sente odore di muffa, è un anfratto buio e tenebroso...')
    time.sleep(2)
    print('Un enorme drago con un balzo ti sbarra il passo...')
    print()
    time.sleep(2)
    
    amico = random.randint(1, num_caverne)
    if CavScelta == str(amico):
        punteggio += 100 * num_caverne
        print(f'''...E con la coda spinge verso di te un grande sacco 
di monete d'oro! Complimenti {nome}, hai guadagnato {punteggio} punti!''')
    else:
        print(f'''...Spalanca le fauci e
ti incenerisce tra mille lingue di fuoco! Mi dispiace {nome}, hai perso!''')
    return punteggio

def main():
    punteggio_totale = 0
    ancora = 's'
    num_caverne = 2

    print("=== IL GIOCO DELLE CAVERNE DEI DRAGHI ===\n")
    nome_giocatore = Intro()

    while ancora == 's':
        print(f"\nLivello attuale: {num_caverne-1}")
        CavNumero = scegliCav(num_caverne)
        punteggio_round = verifica(CavNumero, nome_giocatore, num_caverne)
        punteggio_totale += punteggio_round
        
        print(f'\nPunteggio totale: {punteggio_totale}')
        print('\nVuoi giocare ancora? (s o n)?')
        ancora = input().lower()
        if ancora == 's':
            num_caverne += 1

    print(f'\nGrazie per aver giocato, {nome_giocatore}!')
    print(f'Il tuo punteggio finale è: {punteggio_totale}')

if __name__ == "__main__":
    main()



