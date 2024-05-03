#22
#Le type natif séquentiel (container) str & les exceptions

li = [10, 20, 30, 40] 
#[start:stop:step]
print(li[-1:-4:2], end= '\n') 
print(li[1:5:2], end= '\n')
li.insert(-2,10) 
print(li, end= '\n')
print('\n', '#' * 64, '\n')
#
#23
s = 'Il était une fois ...'
print(s)

li = list(s)
print(li)

s = '\n'.join(li)
print(s)

print('\n', '#' * 64, '\n')
#
#24
li1 = '012345'

li2 = li1
print(li1 == li2)
print(id(li1) == id(li2))

print('*' * 10)

#li3 = li1.copy()                       #AttributeError: 'str' object has no attribute 'copy'
#print(li1 == li3)
#print(id(li1) == id(li3))

li4 = str(li1)
print(li1 == li4)
print(id(li1) == id(li4))

print('\n', '#' * 64, '\n')
#23

from datetime import datetime
dt = datetime.today()

print(dt)
print(str(dt))
print(dt.__str__())
#différentes syntax, même fonctions

print(repr(dt))
print(dt.__repr__())
# retourne le type de la fonction dt + ses valeurs

print('\n', '#' * 64, '\n')

#23

print('Salut \u1019 tout le monde !')
#petit charactère spécial ... oui
print(len('Salut\u1019tout le monde !'))
#RAPPEL len indique le nombre de charactère
print(r'Salut\u0009tout le monde !')
#r empêche l'expression du charactère

s = '\n''***************' '\n'
print(s)

print('012345\r678')
print(len('012345\r678'))

print(15 * '*')

print('Caesar a transmis : \u0027Veni, vidi, vici\u0027 aux sénateurs.')
print('Caesar a transmis : \'Veni, vidi, vici\' aux sénateurs.')
print('Caesar a transmis : "Veni, vidi, vici" aux sénateurs.')
#print('Caesar a transmis : 'Veni, vidi, vici' aux sénateurs.')               #SyntaxError: invalid syntax

#24
#Mécanisme de gestion d'exception

s = '01234501678901'
print(s.count('01'))
print(s.find('01'))
print(s.find('01', 1))
print(s.find('01', 1, 7)) # find retourne -1 car la recherche est hors de la plage.

print('\n', '#' * 64, '\n')
#

#25
#graphe

graphe_matrice = [[0, 1, 1, 0, 1],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 1],
                  [0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 0]]

graphe_dict = {0:[1, 2, 4],
                 1:[0],
                 2:[0, 3, 4],
                 3:[2, 4],
                 4:[0, 2, 3]}

def matrix_to_dict(matrice):
    dictionnaire = {}
    for i in range(len(matrice)):
        dictionnaire[i] = [j for j in range(len(matrice[i])) if matrice[i][j] == 1]
    return dictionnaire

graphe = matrix_to_dict(graphe_matrice)
print(graphe)
print(graphe_dict == graphe)


print('\n', '#' * 64, '\n')

#26
#moyenne

d_cours_id = {'ICS':1, 'Physique':2, 'AL':3, 'GA':4}
d_id_notes = {1:[5,5.5,6,5], 
              2:[3,4.5,5,5.5],
              3:[4,4.5,4.5,5], 
              4:[5,3.5,5,4.5]}

d_cours_moyenne = {}
for cours, id in d_cours_id.items():
    notes = d_id_notes[id]
    moyenne = sum(notes) / len(notes)
    d_cours_moyenne[cours] = moyenne

print(d_cours_moyenne)