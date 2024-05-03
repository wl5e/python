#27
#liste & propriétés

import numpy as np
import matplotlib.pyplot as plt

#objet container de type list
une_liste = [3.14, 'jupyter, saturne', np.dot] # une liste n'est pas forcément homogène
print(une_liste)
print(type(une_liste))
print(hex(id(une_liste[2])))    #'hex' est pour la base hexadécimale, id (adresse mémoire)         
print('*'*50) # t'as capté

une_liste[0] = np.pi                     
#print(une_liste[0,2])     les listes ne peuvent pas être des tuples  => entiers, fractions            
print(une_liste[0:2])                    
print('*'*50)

print(une_liste + [1, 2, np.ones(4), 4])
#print(une_liste + (1,2,np.ones(4),4))   
print('*'*50)

print(5*une_liste[1:2])
#print(une_liste/5)                    

print('\n', '#' * 64, '\n')

#28
#Tableaux unidimensionnels

#créez un tableau (unidimensionnel) y de longueur 20 dont les éléments sont non initialisés
y = np.empty(20)

#affichez le tableau y
print(y)

#fixez les valeurs des quatre premiers éléments à 100 
y[:4] = 100

#donnez aux six éléments suivants des valeurs régulièrement espacées entre 95 et 0
y[4:10] = np.linspace(95,0,6)

# np.linspace(start(intervalle), stop(intervalle), nombres d'échantillons générés)

#attribuez aux 10 éléments suivants les valeurs que prennent les éléments de l'ensemble {0,1,…,9}
#lorsqu'ils sont élevés au carré.
y[10:] = np.arange(10)**2

#affichez le tableau y
print(y)

#représentez graphiquement le tableau y avec les valeurs du tableau en ordonnée et 
#les indices du tableau en abscisse
i = plt.plot(y)

# .plot inverse les valeurs en ordonnée et en absice

#sur ce même graphique, dessinez en vert des lignes brisées verticales aux points 
#𝑥=3, 𝑥=4, 𝑥=9 et 𝑥=10    

for x in [3, 4, 9, 10]:
    plt.plot([x,x],[0,100],'b--') # pour du vert 'g--' etccc

#sur ce même graphique, dessinez en rouge l'axe horizontal (entre 0 et 20) et l'axe vertical (entre 0 et 100)
plt.plot([0,20],[0,0], c = 'cyan') # ligne horizontale
plt.plot([0,0],[0,100], 'cyan') # ligne verticale

#la ligne ci-dessous n'est pas indispensable dans un environnement Jupyter Notebook
plt.show()  

print('\n', '#' * 64, '\n')

#29
#utiliser le fichier texte horaire.txt pour créer un graphe

#importez les données du fichier horaire.txt dans deux tableaux : x (pour la position) et t (pour le temps)
x, t = np.loadtxt('horaire.txt', usecols = (0,1), skiprows = 5, unpack = True)
# .loadtxt('filename',datatype )

#représentez graphiquement les données mesurées (la position en fonction du temps)
plt.xlabel("temps [s]")
plt.ylabel("position [m]")
plt.plot(t,x)
plt.show()

#calculez la vitesse de l'objet en fonction du temps en utilisant la "vectorisation"
v = (x[1:] - x[:1])/(t[1:] - t[:-1])
t_moyen_vit = (t[1:] + t[:1])/2

#v pour déterminer la position en fonction du temps et t_moyen_vit, la moyenne des temps

#calculez l'accélération de l'objet en fonction du temps en utilisant la "vectorisation"
a = (v[1:] - v[:-1])/(t_moyen_vit[1:] - t_moyen_vit[:-1])
t_moyen_acc = (t_moyen_vit[1:] + t_moyen_vit[:-1])/2

#a pour déterminer l'accélération en fonction du temps et t_moyen_acc, la moyenne des temps

#représentez graphiquement la vitesse en fonction du temps
plt.xlabel('temps [s]')
plt.ylabel('vitesse [m/s]')
plt.plot(t_moyen_vit, v, 'g')
plt.show()

#représentez graphiquement l'accélération en fonction du temps

plt.xlabel('temps [s]')
plt.ylabel('accélération [m/s$^2$') # $^2$ permet d'afficher un exposant
plt.plot(t_moyen_acc, a, 'r')
plt.show()

print('\n', '#' * 64, '\n')

#30
#Disposer les éléments d'un array.

m = np.array([[5,2,1,0],[-2,3,9,2],[3,1,4,-2],[6,1,3,3]]) 

#affichez le tableau
print(m)
print('\n')

#affichez l'extension du tableau le long de chaque axe
print(m.shape) 
#donne les dimensions du tableau, ici 4x4 donc (4, 4)
print('\n')

#affichez la troisième ligne du tableau 
print(m[2,:]) #affiche le 2ème élément du tableau ( donc pas le 0eme ou 1er ou ... bref)
print(m[2]) #variant
print('\n')

#affichez la deuxième colonne du tableau 
print(m[:,1]) #affiche la 1ère colonne mais pas la 0ème hein
print('\n')

#affichez le troisième élément de la deuxième ligne du tableau
print(m[1,2])
print('\n')

#affichez les éléments de la sous-matrice 2x2 de m qui se trouve dans le coin en bas à droite
print(m[2:,2:])

print('\n', '#' * 64, '\n')

#31
#Définition d'une fonction pour effectuer un produit matriciel

def calculer_PM(A, B):
    '''
    Paramètres : 
        matrice A de taille m*n
        matrice B de taille n*p
    Résultat retourné : 
        matrice produit C=A*B de taille m*p
    '''
    if(A.shape[1] != B.shape[0]):
        raise Exception('Argments non valides !')
    
    C = np.empty((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for k in range(B.shape[1]):
            C[i,k] = sum(A[i,:]*B[:,k])
    return C

#Exécution de la fonction calculer_PM

try: # try permet de tester le code
    A = np.array([[1 , 2, 0], [4, 3, -1]])
    B = np.array([[5, 1], [2, 3], [3,4]])
    print (calculer_PM(A,B))
    print('********************************')
    A = np.array([[6, -2, 5, 2], [4, -3, 1, 3]])
    B = np.array([[-1 , 6, 5], [4, 7, -2], [0, 8, 9], [1, 10, 11]])
    print (calculer_PM(A,B))
    print('********************************')
    A = np.array([[3]])
    B = np.array([[5]])
    print (calculer_PM(A,B))
    print('********************************')
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [0, 9]])
    print(calculer_PM(A,B))
    print('********************************')
    A = np.array([[]])
    B = np.array([[]])
    print(calculer_PM(A,B))
    print('********************************')
except Exception as ex:
    print(ex)
print('********************************')

print('\n', '#' * 64, '\n')

#32
#Déterminer le temps d'exécution de la fonction calculer_PM

import timeit

A = np.array([[5,2,1,0],[-2,3,9,2],[3,1,4,-2],[6,1,3,3]])
B = np.array([[2,4,-1],[15,2,5],[1,1,4],[7,10,-2]])
print(calculer_PM(A,B))
print('\n********************************')
print(calculer_PM(A,B) == np.dot(A,B))
print('\n********************************')

t_ad_hoc = timeit.timeit(stmt = 'calculer_PM(A,B)', number=100_000, globals=globals())
t_np = timeit.timeit(stmt = 'np.dot(A,B)', number=100_000, globals=globals())
print(f'Le temps pour les 100\'000 appels ad hoc : {t_ad_hoc} secondes.')
print(f'Le temps pour les 100\'000 appels NumPy : {t_np} secondes.')
print(f'Les 100\'000 appels NumPy ont été {t_ad_hoc/t_np} plus rapides que les 100\'000 appels ad hoc !')
