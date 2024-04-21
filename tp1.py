#04
print("Introduisez l'an de l'assasinat de Caesar :")
#la bonne réponse est -44 !
an = input()
print(type(an)) #on veut connaître le type de la variable an
print('Caesar a été assasiné en :', an, '!')

print('Caesar a été assasiné il y a', 2020 - int(an), 'ans.')

#05

# Rappel ! Les variables ont été déclarées plus haut c:
# Le double étoile(**) signifie "exposant"

import math
rayon = 10
hauteur = 20
type(math.pi)
vol = math.pi*rayon**2*hauteur

#06
# additionner les surfaces "deux sphères et rectangle"
aire_tot = 2*math.pi*rayon**2 + 2*math.pi*rayon*hauteur

print('Un cylindre de rayon', rayon, 'et hauteur', hauteur, '!')
print('Son volume vaut', vol, 'et son aire totale vaut', aire_tot, '!')
print('\nLe volume de celui-ci est de : ', vol, 'm')

# Il y'a egalement la possibilité d'utiliser "round" pour avoir un résultat 
# à deux décimales, trois décimales, etccc

print('\nUn cylindre de rayon', round(rayon,2), 'et hauteur', round(hauteur,2), '!')
print('Son volume vaut', round(vol,3), 'et son aire totale vaut', round(aire_tot,2), '!')

#07
