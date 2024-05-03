#00
# Affichage d'un message de bienvenue simple.

print("Exercice 00 : Affichage d'un message de bienvenue simple.\n")
print('Hello, World!')
print('\n', '#' * 64, '\n')

#01
# Utilisation de la fonction print() pour afficher une citation de César.
# La fonction end=', ' est utilisée pour éviter le saut de ligne après chaque print().

print("Exercice 01 : Affichage d'une citation de César.\n")
print('Casear dixit : "Veni, vidi, vici".')

print('Veni', end=', ')
print('vidi', end=', ')
print('vici!')
print('\n', '#' * 64, '\n')

#02
# Utilisation de la fonction input() pour obtenir une entrée de l'utilisateur.
# L'entrée est ensuite affichée à l'écran.

print("Exercice 02 : Utilisation de la fonction input() pour obtenir une entrée de l'utilisateur.\n")
print('Introduisez votre nom :')
rep = input()
print('Votre nom est :', rep, '. Vraiment distingué !')
print('\n', '#' * 64, '\n')

#03
# Importation de la bibliothèque math pour accéder à la constante pi.
# Affichage de la valeur de pi et de son type.

import math
print(math.pi)
type(math.pi)