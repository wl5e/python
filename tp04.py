#14
# Consigne : Méthode d'indexation
print("\nExercice 14 : Méthode d'indexation")

lis = [10, 11, 12]
    # [ 0 , 1 . 2]

print('la liste est :[10, 11, 12]')
print(lis.append(14)) # ajoute UN ET UN  SEUL ET UNIQUE élément "14" dans la liste
# renvoie un None (opération)
print(lis) # renvoie les élements de la liste
print('-' * 58) # ---....
print(lis.insert(2, 100)) # insère 100 à la 2ème position(index = 2) dans la liste
# renvoie un None (opération)
print(lis.extend([22, 23])) # ajoute 22 et 23 dans la liste, PLUSIEURS ELEMENTS (en fin de liste)
# renvoie un None (opération)
print(lis * 2) # affiche tous les élements de la liste en double, mais NE LA DOUBLE PAS VRAIMENT !
print('-' * 58) # ----...
print(lis.pop()) # renvoie et supprime le dernier index (23 dans ce cas)
print(lis)
print(lis.pop(1)) # renvoie et supprime le 1er index ( DONC PAS LE 0 EME !)
print(lis)
print(lis.remove(10)) # supprime le 10 de la liste donc INDEX = 0,
#print(del lis[0])          #SyntaxError: invalid syntax  
print(lis)
print('-' * 58) # ----....
del lis[0] # supprime l'élement de l'index 0 de la liste
print(lis) # affiche la liste sans l'élément précédemment supprimé
print(lis.reverse()) #retourne les éléments de la liste
lis.reverse() # retourne encore la liste sans appel au print
lis.reverse() # retourne une nouvelle fois la liste toujours sans appel au print
print(lis)
print('-' * 58) # ---...
print(lis.copy()) # imprime une copie de la liste
print(lis.clear()) # supprime les éléments de la liste
print(lis)


# Consigne : Packing et Unpacking
print("\nExercice : Packing et Unpacking")

val1, val2 = 10, 11
print('val1 =', val1, 'val2 =', val2)

print('*' * 20)

# val1, val2 = 10, 11, 12, 13, 14, 15  ça n'a pas de sens   

values = 10, 11, 12, 13, 14, 15 # On déclare une variable values à laquelle on attribue plein de valeurs
print(values)

a, b, _, c, _, d = values # on réatribue le paquet de valeurs : a = 10, b = 11, _ = 12, c = 13
# puis la valeur de _ est modifiée pour devenir 14 (La dernière valeure attribuée), d = 15
print('c =', c)
print('_ =', _,"\ncar il s'agit de la dernière valeur attribuée")

print('*' * 20)

x, y, *suite, z, _ = values # même délire sauf qu'il faut considérer que *suite prend une intervalle,
# sa valeur et celle de juste après, en l'occurence [12, 13] donc 12 et 13
print('x =', x, 'y =', y, 'z =',z)
print('suite =', suite)
print(type(suite))


#Tuple (immutable) avec un élément immutable et un élément mutable

tup = 10, [11, 12] # attention, seulement [11, 12] sont dans un tableau
print(type(tup))
print(id(tup[1]))
print(tup)
#tup[0] = 20  ce n'est pas un tableau              
#tup[1] = [111, 222] manque des arguments et les valeurs ne doivent pas être encadrées       
tup[1][0] = 22             
print(tup)
tup[1].append(13)
print(tup)
tup[1].clear()

print('*' * 18)

print(tup)
#tup[1] = [31, 32, 33]    foireux de toute façon  
tup[1].extend([31, 32, 33])
print(tup)
print(id(tup[1])) #ne changera pas
print('\n', '#' * 64, '\n')


#15
# Consigne : Trouver le minimum et le maximum d'une liste de nombres
print("\nExercice 15 : Trouver le minimum et le maximum d'une liste de nombres")
#récupérez et stockez les nombres introduits par l'utilisateur dans un container approprié ;
#utilisez des fonctions (prédéfinies) natives appropriées afin de trouver le maximum et le minumum des nombres introduits ;
#affichez les résultats ainsi calculés.

nb = int(input("Combien de nombres réels voulez-vous introduire, s.v.p. : "))

maxim = float('-inf')
print('Au début, le maximum vaut :', maxim)
minim = float('InFinitY')
print('Au début, le minimum vaut :', minim)

for i in range(nb):
    nombre = float(input("Entrez le nombre numéro " + str(i+1) + ", s.v.p. : "))
    if nombre > maxim:
        maxim = nombre
    if nombre < minim:
        minim = nombre
        
print('\nLe maximum est :', maxim, '!')
print('Le minimum est :', minim, '!')

# Consigne : Définir une fonction pour trouver le minimum d'une liste
print("\nExercice : Définir une fonction pour trouver le minimum d'une liste")
def my_min(lis):
    min = lis[0] # on considère le minimum comme étant la valeur de l'index 0 de la liste
    for i in lis:
        if i < min: # si l'élément de la liste est plus petit EN VALEUR que l'index 0, alors
            min = i # la valeur de l'index sera alors attribué à min et deviendra le nouveau min !
    return min

#élaborer les fonctions avec les différentes listes comme argument !
print("\nle minimum : ", my_min([-3.2, 11, 0, 22.3, 4.8]))
print("le minimum : ", my_min([3.14, 3.14, 3.14]))
print("le minimum : ", my_min(['tata', 'toto premier', 'titi le grand'])) # fonctionne en nbr de charactere :)
#print("le minimum : ", my_min(['tata', -3.2, 'toto', 53.8])) ça ne marchera pas non plus


# archi basique ...
# Consigne : Définir une fonction pour trouver le minimum et le maximum d'une liste
print("\nExercice : Définir une fonction pour trouver le minimum et le maximum d'une liste")
def min_max(lis):
    return min(lis), max(lis)

# Pour rappel les tuples à la différence des listes ne sont pas mutables, une fois que la collection
# ordonnée des élements est établie !

print('\nLe tuple (minimum, maximum) :', min_max([-3.2, 11, 0, 22.3, 4.8]))
print('Le tuple (minimum, maximum) :', min_max([3.14, 3.14, 3.14]))
print('Le tuple (minimum, maximum) :', min_max(['tata', 'toto premier', 'titi le grand'] ))
# print('Le tuple (minimum, maximum) :', min_max(['tata', -3.2, 'toto', 53.8]))
