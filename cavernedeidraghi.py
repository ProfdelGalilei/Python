# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:30:34 2020

@author: federica
"""

import random
import time
def Intro():
    print ('''Dopo un lungo cammino, si erge di fronte a te la montagna dei 
           draghi. Tra una folta boscaglia, vedi il sentiero che si biforca e
           scorgi in lontananza, in fondo a ciascun sentiero, una caverna. 
           La leggenda racconta che in una di queste caverne si trova un drago
           pericolosissimo, mentre nell’altra c’è un drago buono, 
           che regala monete d’oro dal suo tesoro a tutti i visitatori…''')
    print()

def scegliCav():
    caverna =''
    while caverna != '1' and caverna != '2':
        print ('In quale caverna vuoi entrare? 1 o2?')
        caverna = input()
        
     
    
def verifica(CavScelta):
    print ('Ti avvicini con cautela alla caverna...')
    time.sleep(2)
    print ('Si sente odore di muffa, è un anfratto buio e tenebroso...')
    time.sleep(2)
    print ('Un enorme drago con un balzo ti sbarra il passo...')
    print()
    time.sleep(2)
    
    amico = random.randint(1,2)
    if CavScelta == str (amico):
        print ('''...E con la coda spinge verso di te una grande sacco 
               di monete d'oro''')
    else:
        print (''' ...Spalanca le fauci e
               ti incenerisce tra mille lingue di fuoco!''' )
    
ancora = 's'
while ancora == 's':
    Intro()
    CavNumero = scegliCav()
    verifica(CavNumero)
    print('Vuoi giocare ancora? (s o n)?')
    ancora = input()
    
    
