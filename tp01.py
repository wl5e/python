#04
# Consigne : Demandez à l'utilisateur l'année de l'assassinat de César.
print("Exercice 04 : Demandez à l'utilisateur l'année de l'assassinat de César.")
print("\nIntroduisez l'an de l'assasinat de Caesar :")
#La bonne réponse est -44 ! Ceci est une question d'histoire, pas de programmation.

an = input()
print(type(an)) # Affiche le type de la variable 'an'. Il devrait être str car input() renvoie une chaîne.

print('\nCaesar a été assasiné en :', an, '!')
print('Caesar a été assasiné il y a', 2020 - int(an), 'ans.')
print('\n', '#' * 64, '\n')

#05
#Rappel ! Les variables ont été déclarées plus haut c:
# Consigne : Calculez le volume d'un cylindre.
#Le double étoile(**) signifie "exposant". Il est utilisé pour calculer la puissance.

print("Exercice 05 : Calculez le volume d'un cylindre.")
import math
rayon = 10
hauteur = 20
type(math.pi)
vol = math.pi*rayon**2*hauteur

#06
# Consigne : Calculez l'aire totale d'un cylindre.
print("\nExercice 06 : Calculez l'aire totale d'un cylindre.")
aire_tot = 2*math.pi*rayon**2 + 2*math.pi*rayon*hauteur # Calcul de l'aire totale d'un cylindre.

print('Un cylindre de rayon', rayon, 'et hauteur', hauteur, '!')
print('Son volume vaut', vol, 'et son aire totale vaut', aire_tot, '!')
print('\nLe volume de celui-ci est de : ', vol, 'm')

#Il y'a egalement la possibilité d'utiliser "round" pour avoir un résultat 
#À deux décimales, trois décimales, etccc

print('\nUn cylindre de rayon', round(rayon,2), 'et hauteur', round(hauteur,2), '!')
print('\nSon volume vaut', round(vol,3), 'et son aire totale vaut', round(aire_tot,2), '!')
print('\n', '#' * 64, '\n')

#07
# Consigne : Affichez la date d'aujourd'hui.
from datetime import date

print("Exercice 07 : Affichez la date d'aujourd'hui.")
aujourd_hui = date.today()
print(type(aujourd_hui))
print(aujourd_hui,'\n')

#Introduction des données
# Consigne : Demandez à l'utilisateur d'introduire son nom et son prénom.
print("Exercice : Demandez à l'utilisateur d'introduire son nom et son prénom.")
print("\nBonjour ! C'est du code Python !")
nom = input('\nIntroduisez votre nom, svp :\n')
prenom = input('Introduisez votre prénom, svp :\n')
annee_naissance = input('Introduisez votre année de naissance, svp :\n')
#Traitement des données

#print(date.today())

an_courant = date.today().year

age = an_courant - int(annee_naissance)
#Affichage des résultats
print('Bonjour', prenom, nom, '!', '\nVous avez', age, 'ans !', '\nAu revoir !')


