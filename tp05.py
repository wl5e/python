#16
# Consigne : Copie superficielle d'un set
print("\nExercice 16 : Copie superficielle d'un set")
se = {3, 'un', 'deux',4} #dictionnaire planqué "imprévisible", la clé est un hash
# {}, c'est un set. [] c'est des listes.

se_cop = se.copy()
print(se)
print(se_cop)
print('*' * 30)
print(se == se_cop)
print(id(se) == id(se_cop)) #vérifie si les adresses mémoires (identifiants) sont les mêmes
print('*' * 30)
se_cop.add(9.99)
print(se)
print(se_cop)

# Consigne : Copie superficielle d'un dictionnaire
print("\nExercice : Copie superficielle d'un dictionnaire")
dic = {'je':'ich', 'elle':'sie'} # la clé peut être un chiffre aussi
dic_cop = dic.copy()
print(dic)
print(dic_cop)
print('*' * 45)
print(dic == dic_cop)
print(id(dic) == id(dic_cop))
print('*' * 45)
dic_cop['elle'] = 'she' # change la valeur liée à la clé 'elle' : sie -> she
dic_cop['nous'] = 'wir' # ajoute une clé 'nous' avec une valeur 'wie'
print(dic)
print(dic_cop)         # affiche les deux dictionnaires
print('*' * 30)
print(dic.values()) # affiche les valeurs d'un dictionnaire sans les clés c:

print('\n', '#' * 64, '\n')

#17
# Consigne : Définir une fonction nommée inverser()
print("\nExercice 17 : Définir une fonction nommée inverser()")
#les clés du dictionnaire résultat sont les valeurs du dictionnaire argument;
#les valeurs du dictionnaire résultat sont les dlés du dictionaire argument.

#Définition de inverser() :

#définisez ci-dessous la fonction inverser
champion = {'tnasialpmoc' : 'complaisant', 'kcid' : 'dick', 'pussy' : 'dick', 'peasant' : 'EPFL'}
pogchamp = {'tnasialpmoc' : 'complaisant', 'kcid' : 'dick', 'peasant' : 'EPFL'}

# champion, pogchamp sont des dictionnaires

#def inverser(dic) : 
#    for val0 in dic.values():
#        for val1 in dic.values():
#            if val0 == val1 :
#                return {} # dès qu'il touche un return. L'interpréteur sort de la fonction 
#    
#    newdic = {}
#    for val0 in dic.values():
#        dic.values() == dic.keys

#newchamp = inverser(champion) 
#print(newchamp)
#print(inverser(pogchamp))

# méthode foireuse mdrr

def inverser(dic) :
    list_keys = list(dic.keys())
    list_vals = list(dic.values())
    set_vals = set(list_vals)

    if(len(list_vals) != len(set_vals)):
        # la fonction len donne le nombre d'éléments de la liste (ou du set)
        return {}
    return {dick:pussy for pussy,dick in dic.items()}
    # inverse les clés et les valeurs, osef de mentionner spécifiquement "valeurs et clés" ... 

print(inverser(champion))
print(inverser(pogchamp))

#Définition de fonction inverser() :

osef = {'un':1, 'deux':2, 'trois':3}

#affichez l'objet associé au nom dico
print(osef)

#affichez le résultat obtenu par un appel de la fonction inverser
#avec dico comme argument effectif
print(inverser(osef))

print('*' * 45)

osef['uno'] = 1

#affichez l'objet associé au nom dico
print(osef)

#affichez le résultat obtenu par un appel de la fonction inverser
#avec dico comme argument effectif
print(inverser(osef))

#petite nuance entre le dico et une liste
print('\n', '#' * 64, '\n')

#18
# Consigne : Ecrire un programme interactif
print("\nExercice 18 : Ecrire un programme interactif")
print('\nBonjour ...')

dic={}
#utiliser les propriétés de true or false
while True :
    pays = input('Introduisez le pays s.v.p. (stop est le dernier élément) : ')
    if pays == 'stop':
        break
    capitale = input('Introduisez la capitale du pays s.v.p. : ')
    #introduire les clés et valeurs dans le dico ( pays et capitale)
    dic[pays] = capitale

print('\n \n Vous avez introduit toutes les données suivantes :')
print(dic)

print('\n \n Vous avez introduit les pays suivants :')
print(list(dic.keys()))

print ('\n \n Vous avez introduit les capitales suivanes :')
print(list(dic.values()))
print('\n', '#' * 64, '\n')

#19
# Consigne : Ecrire une fonction reussir() et l'appeler
print("\nExercice 19 : Ecrire une fonction reussir() et l'appeler")

#nom=input('Entrez le nom :')
#notes[0]=input('\n entrez la 1ère note:')
#notes[1]=input('\n entrez la 2ème note:')

def reussir(dic):
# la principale difficulté réside dans le fait qu'il faille entrer 2 notes
    dic_moyennes = {nom :(notes[0]+notes[1])/2 for nom, notes in dic.items()}

    # |nom |note0, note1, .... -> nom:moyenne
    dic_4 = {nom:moyenne for nom, moyenne in dic_moyennes.items() if moyenne >= 4}

    #prend en considération que les moyennes au-dessus de 4

    return dic_moyennes, dic_4

#on vous donne les paires noms:notes pour les étudiants
students = {'toto':[5,6], 'gigi':[4.5,5.5], 'titi':[3.5,4], 'tata':[6,6]}

#appelez la fonction reussir avec la variable locale students comme argument
students_moyennes, students_4 = reussir(students)
#students moyennes est associté à dic_moyennes de la fonction. students_4 lui est associé à dic_4

#affichez les paires noms:moyennes pour tous les étudiants
print("\n", students_moyennes)

#affichez les paires noms:moyennes seulement pour les étuudiants promus
print("\n", students_4)
print('\n', '#' * 64, '\n')

#20
# Consigne : Ecrire une fonction qui prend en argument un dictionnaire et qui retourne un autre dictionnaire
print("\nExercice 20 : Ecrire une fonction qui prend en argument un dictionnaire et qui retourne un autre dictionnaire")
def fib_iter(n):
    old , new = 0, 1    #deux variables old = 0 et new =1
    if n == 0:          
        return 0        #si n = 0, alors fib_iter retourne 0
    for i in range (n-1):   #de l'index 0 à n-1 ...
        print(old, end=' ') #imprime old, '0'. (et end = ' ', pour l'espace j'imagine ... enfin bref) 
        old, new = new, old+new # old = new, new = old + new
        # par exemple, n=4 (3ème itération) old -> 1 et new ->3
    return new #retourne la dernière valeur de new
print("\nLes 12 premiers chiffres de la suite de fibonnaci sont :\n")
print( fib_iter(12))
#

import timeit
def fib_iter(n):
    old , new = 0, 1
    if n == 0:
        return 0
    for i in range (n-1):
        old, new = new, old+new        
    return new
print("\nLe temps nécessaire : ")
print(str(timeit.timeit(stmt = 'fib_iter(12)', number=100_000, globals=globals())) 
                                                                   + ' secondes.')
#
# fonctions utiles pour déterminer le temps d'éxécution.

#C'est plus long

def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

print("\nLe temps nécessaire :")
print(str(timeit.timeit('fib_rec(12)', number=100_000, globals=globals())) 
                                                            + ' secondes')
#
def fib_rec_plus(n, dic):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n in dic :
        return dic[n]
    
    dic[n] = fib_rec_plus(n-1, dic) + fib_rec_plus(n-2, dic)
    return dic[n]
print("\nLa valeur du 12ème élément de la suite de Fibonacci est : ")
print(fib_rec_plus(12, {}))

#copié, collé => flemme !
print("\nLe temps nécessaire : ")
print(str(timeit.timeit('fib_rec_plus(12, {})', number=100_000, globals=globals()))
                                                               + ' secondes.\n')
print('\n', '#' * 64, '\n')

#21
# Consigne : Définir la fonction combiner et l'appeler avec différents arguments
print("\nExercice 21 : Définir la fonction combiner et l'appeler avec différents arguments")
#définissez la fonction combiner
name = ['']
vorname = ['']

def combiner(lis_name, lis_vorname):
    if len(lis_name) != len(lis_vorname):
        # vérifie si les listes ont le même nombre d'éléments
        return [];
    l_res = [lis_name[i] + ' ' + lis_vorname[i] for i in range (len(lis_name))]
    return l_res
print(combiner(name, vorname))

#

noms = ['Bonnet', 'Blanc', 'Neige']
prenoms = ['Blanc', 'Bonnet', 'Blanche']
surnoms = ['BB', 'NB']

#affichez le résultat retourné par l'appel de la fonction combiner 
#avec les listes noms et prenoms comme arguments effectifs
#et affichez une liste

print(combiner(noms,prenoms),surnoms)

#affichez le résultat retourné par l'appel de la fonction combiner 
#avec les listes noms et surnoms comme arguments effectifs

print(combiner(noms, surnoms))

#

li = [[n * m for n in range(1, 6)] for m in range(1, 6)]
#dont use the last range number (1, X)
print(li)
print('-' * 128)
lim = [print(toto) for toto in li]
#ne veut rien dire

#res = print(lim)
print('-' * 128)
#print(res)