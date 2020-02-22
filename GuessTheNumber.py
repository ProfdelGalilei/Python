# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# questo gioco fa indovinare un numero.
import random
 
tentativi = 0
 
print('Ciao, come ti chiami?')
nome = input()
 
number = random.randint(1, 20)
print('Bene, ' + nome + ', sto pensando un numero tra 1 e 20.')

for tentativi in range(6):
     print('Prova a indovinare.') # Four spaces in front of "print"
     guess = input()
     guess = int(guess)

     if guess < number:
         print('Troppo basso.') # Eight spaces in front of "print"

     if guess > number:
         print('Troppo alto.')
         
     if guess == number:
         break

if guess == number:
     tentativi = str(tentativi + 1)
     print('Ottimo, ' + nome + '! Hai indovinato in ' +
          tentativi + ' tentativi!')

if guess != number:
     number = str(number)
     print('Non hai vinto. Il numero che stavo pensando è ' + number + '.')