#33

import numpy as np
import matplotlib.pyplot as plt

# Utiliser la fonction Python bissection() pour trouver un zéro de la fonction f.

def f(x):
    return x/10 - np.sin(x) + 0.25
# definition de la fonction

x = np.linspace(-20, 20, 100)
y = f(x)

# np.linspace(start, stop, nombre d'échantillons (points) générés)

plt.figure(figsize=(14, 6))
# <Figure size 1008x432 with 0 Axes>
plt.plot(x, y, label='f(x)')
# présente les axes
plt.plot([x[0], x[-1]], [0,0], c='0.72')
# présente un axe horizontal en en y=0
plt.plot([0,0], [y.min(),y.max()], c='0.72')
# présente un axe vertical en x=0
plt.xlabel('x')
plt.ylabel('f(x)')
#évident
plt.legend(loc='best')
# en haut, à droite
plt.show()

print('\n', '#' * 64, '\n')

x = np.linspace(0, np.pi/2, 300) 
# de 0 à 1.57
y = f(x)

plt.plot(x,y, label='f(x)')
plt.plot([x[0],x[-1]], [0,0], c='0.72')
plt.plot([0,0], [y.min(),y.max()], c='0.72')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='best')
plt.show()

print('\n', '#' * 64, '\n')

a, b = 0, np.pi/2
e = 1e-6
# e est pour epsilon
print(np.log2((b-a)/e)-1)

def dessiner_PF(g, x0, nb, couleur):
    '''
    But : visualiser les nb premières itérations de la méthode de Picard
    Paramètres : 
        g : la fonction étudiée
        x0 : la valeur de départ 
        nb : le nombre d'itérations prévues
        couleur : la couleur des traits
    Retourne : 
        un dessin avec un point (correspondant au point de départ) et
        2*nb segments de couleur
    '''    
    plt.plot([x0], [x0], color = couleur, marker='o')
    for i in range(nb):
        x1 = g(x0)
        plt.plot([x0,x0], [x0,x1], color = couleur)
        plt.plot([x0,x1], [x1,x1], color = couleur)
        x0 = x1

# dessiner_PF(np.cos, 0.5, 10, 'r')

def bissection(f, a, b, eps, n):
    '''
    But : 
        trouver une solution approchée de l'équation f(x)=0 
           sur l'intervalle [a,b] par la méthode de la bissection simple
    Paramètres : 
        f : la fonction pour laquelle on cherche un zéro
        a et b : les bornes de l'intervalle initial de recherche
        eps : la tolérance à satisfaire
    Retourne : 
        x : la valeur approchée d'un zéro de f
        n : le nombre d'itérations effectuées
    '''    
    if f(a)*f(b) >= 0:
        raise Exception('L\'intervalle de départ non valide !')
        
    if a > b:
        a, b = b, a
        
    n = 0
    x = (a+b)/2   
    while abs(b-a)/2 >= eps:       
        if f(x) == 0:
            print('La solution calculée est exacte !')
            return x, n
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        x = (a+b)/2
        n += 1
    return x, n   

print("\nThe bissection method gives the following result : ")
print(bissection(f, 0, np.pi/2, 1e-6, n=0))

#

def bissection_plus(f, a, b, step, eps):
    '''
    But : 
        trouver une (ou plusieurs) solution(s) approchée(s) de l'équation f(x)=0 
           sur l'intervalle [a,b] par la méthode de la bissection par intervalles
        cette fonction utilise la fonction bissection() sur les sous-intervalles "valides"
    Paramètres : 
        f : la fonction pour laquelle on cherche le(s) zéro(s)
        a et b : les bornes de l'intervalle initial de recherche 
        step : la longueur de chacun des intervalles considérés
        eps : la tolérance à satisfaire
    Retourne : 
        zeros : une liste qui contient le(s) zéro(s)
    ''' 
    x = np.arange(a, b+step, step)
    zeros = []
    for i in range(x.shape[0]-1):
        a_i = x[i]
        b_i = x[i+1]
        if f(a_i)*f(b_i) < 0:
            zeros.append(bissection(f, a_i, b_i, eps)[0])
    return zeros

print('\n', '#' * 64, '\n')

#34

def g(x):
    return np.log(x**2)+x-9
    # l'exposant emploie cette nnotation : ** et pas ^ .

x = np.linspace(0.2, 10, 1000)
y = g(x)

plt.plot(x, y, label='f(x)')
plt.plot([0,x[-1]], [0,0], c='0.72')
plt.plot([0,0], [y.min(),y.max()], c='0.72')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend(loc='best')
plt.show()

print('\n', '#' * 64, '\n')

a0, b0 = 0.2, 10
eps = 1e-7
print("Le nombre minimal d'itérations nécessaires est : n_min >", np.log2((b0-a0)/eps)-1)

res = bissection(f, a0, b0, eps, nb=0)
print('Zéro trouvé par la méthode de la bissection simple : x =', res[0])
print("Le nombre d'itérations effectuées est : n_eff =", res[1])

print('\n', '#' * 64, '\n')

#35

#Programme pour déterminer les zéros des précédentes fonctions

def f(x):
    return x/10 - np.sin(x) + 1/4

a, b = -10, 5
eps = 1e-6

# De manière à ne pas "perdre" de zéros, nous choisissons un pas suffisamment petit entre les
# différents intervalles, par exemple, un pas de 0.1.
pas = 0.1

solutions = bissection_plus(f, a, b, pas, eps)

print('\nLe programme a permis de trouver', len(solutions), 'zéros :\n')
for indice in range(len(solutions)):
    print('x_'+str(indice+1), '=', str(solutions[indice]),'\n')

print('\n', '#' * 64, '\n')

#afficher sur le graphe les zéros trouvés

x = np.linspace(a, b, 100)
y = f(x)

plt.figure(figsize=(14, 6))
plt.plot(x, y, label='f(x)')
plt.plot([x[0],x[-1]], [0,0], c='0.72')
plt.plot([0,0], [y.min(),y.max()], c='0.72')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='best')

for indice in range(len(solutions)):
    plt.plot(solutions[indice], f(solutions[indice]),'ro')

plt.show()

print('\n', '#' * 64, '\n')

# fonctions supémentaires ...

def f(x):
    return np.cos(1/x)

x = np.linspace(-1, -0.05, 1000) 
y = f(x)

plt.figure(figsize=(14, 5))
plt.plot(x, y, label='f(x)')
plt.plot([x[0],x[-1]], [0,0], c='0.72')
plt.plot([0,0], [y.min(),y.max()], c='0.72') 
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(loc='best')
plt.show()

#affichage

a, b = -1, -0.05
eps = 1e-6

# De manière à ne pas "perdre" de zéros, nous choisissons un pas suffisamment petit entre les
# différents intervalles, par exemple, un pas de 0.01. (à expérimenter !)
pas = 0.01

solutions = bissection_plus(f, a, b, pas, eps)

print('\nLe programme a permis de trouver', len(solutions), 'zéros.\n')
for indice in range(len(solutions)):
    print('x_'+str(indice+1),'=',str(solutions[indice]),'\n')
