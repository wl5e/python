#04
print("Introduisez l'an de l'assasinat de Caesar :")
#La bonne réponse est -44 !
an = input()
print(type(an)) #on veut connaître le type de la variable an
print('Caesar a été assasiné en :', an, '!')

print('Caesar a été assasiné il y a', 2020 - int(an), 'ans.')

#05
#Rappel ! Les variables ont été déclarées plus haut c:
#Le double étoile(**) signifie "exposant"

import math
rayon = 10
hauteur = 20
type(math.pi)
vol = math.pi*rayon**2*hauteur

#06
#Additionner les surfaces "deux sphères et rectangle"
aire_tot = 2*math.pi*rayon**2 + 2*math.pi*rayon*hauteur

print('Un cylindre de rayon', rayon, 'et hauteur', hauteur, '!')
print('Son volume vaut', vol, 'et son aire totale vaut', aire_tot, '!')
print('\nLe volume de celui-ci est de : ', vol, 'm')

#Il y'a egalement la possibilité d'utiliser "round" pour avoir un résultat 
#À deux décimales, trois décimales, etccc

print('\nUn cylindre de rayon', round(rayon,2), 'et hauteur', round(hauteur,2), '!')
print('Son volume vaut', round(vol,3), 'et son aire totale vaut', round(aire_tot,2), '!')

#07
#La classe date définit du module datetime.

from datetime import date

aujourd_hui = date.today()
print(type(aujourd_hui))
print(aujourd_hui,'\n')

#Introduction des données
print("Bonjour ! C'est du code Python !")
nom = input('Introduisez votre nom, svp :\n')
prenom = input('Introduisez votre prénom, svp :\n')
annee_naissance = input('Introduisez votre année de naissance, svp :\n')
#Traitement des données

#print(date.today())

an_courant = date.today().year

age = an_courant - int(annee_naissance)
#Affichage des résultats
print('Bonjour', prenom, nom, '!', '\nVous avez', age, 'ans !', '\nAu revoir !')


