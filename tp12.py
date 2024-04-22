#Equations différentielles ordinaires (EDO)

import numpy as np
import matplotlib.pyplot as plt

#Schémas d'Euler progressif, Euler retrograde et Runge-Kutta d'ordre 4 (RK4)

def visualiser_EDO(t, u, y=None, x_lim=None, y_lim=None):
    '''
    But :
       représenter graphiquement la solution approchée (et éventuellement la solution exacte)
           d'un problème de Cauchy
    Paramètres :
       t : un vecteur (1D array) avec les valeurs discrètes du temps 
       u : un vecteur (1D array) avec les valeurs discrètes de la solution approchée 
       y : la fonction solution exacte
       x_lim : un tuple avec les limites de l'axe des abscisses
       y_lim : un tuple avec les limites de l'axe des ordonnées
    Retourne :
       la représentation graphique de la solution approchée (et éventuellement de la solution exacte) 
           du problème de Cauchy
    ''' 

    if y:
        t_exacte = np.linspace(t[0], t[-1], 100)
        y_exacte = y(t_exacte)
        plt.plot(t_exacte, y_exacte, color='b', label='solution exacte')
        plt.title(F'Solution exacte vs solution approchée (N = {len(t)-1} sous-intervalles)')
        plt.ylabel('solutions (exacte et approchée)')
    else:
        plt.title(F'Solution approchée (N = {len(t)-1} sous-intervalles)') 
        plt.ylabel('solution approchée')
    
    plt.plot(t, u, color='r', label='solution approchée') 
    for i in range(len(t)):
        plt.plot(t[i], u[i], '.r')
    
    plt.axhline(u[0], c='g')
    plt.axvline(t[0], c='g')
    plt.legend(loc='best')
    plt.xlabel('$t$')
    plt.grid(True)
    if x_lim :   
        plt.xlim(x_lim)
    else:
        plt.xlim(t[0],t[-1])
    if y_lim:
        plt.ylim(y_lim)
    else:
        if y:
            plt.ylim(min(min(u), min(y_exacte)), max(max(u), max(y_exacte)))
        else:
            plt.ylim(min(u), max(u))

#Représentation graphique de la solution exacte

def y(t):
    return (t-1)**2*np.exp(t)

###

t0, T = 0, 2.1
t = np.linspace(t0, T, 10000)

plt.figure(figsize=(8,5))
plt.plot(t, y(t), color='b', label=R'$y(t)=(t-1)^2e^t$')
plt.title('La solution exacte')
plt.legend(loc='best')
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.grid(True)
plt.xlim(t0, T)
plt.ylim(0, 10)
plt.show()

#Représentation graphique de la solution exacte et de la pente

def f(t, y):
    return y+2*(t-1)*np.exp(t)

###

t0, T = 0, 2.1
t = np.linspace(t0, T, 101)

plt.figure(figsize=(8,5))
plt.plot(t, y(t), color='b', label='La solution exacte')
plt.plot(t, f(t, y(t)), color='m', label='La pente')
plt.title('La solution exacte et la pente')
plt.legend(loc='best')
plt.xlabel('$t$')
plt.ylabel('$y, f$')
plt.grid(True)
plt.xlim(t0, T)
#plt.ylim(0, 10)
plt.show()

#Schéma explicite à un pas d'Euler progressif euler_pro()

def euler_pro(f, t0, y0, T, N):
    '''
    But : 
        résoudre un problème de Cauchy par la méthode d'Euler progressive
    Paramètres : 
        f : la pente (la dérivée) de la solution
        t0 : le moment initial
        y0 : la valeur initiale
        T : la durée d'étude
        N : le nombre de sous-intervalles
    Retourne : 
        t : le vecteur (1D array) avec les points où la solution approchée a été calculée
        u : le vecteur (1D array) avec les valeurs approchées de la solution         
    '''  
    t, h = np.linspace(t0, T, N+1, retstep=True)
    u = np.empty(N+1)
    ## vide l'array
    u[0] = y0  
    for n in range(N):
        u[n+1] = u[n] + h*f(t[n], u[n])
    return t, u 

#Schéma implicite à un pas d'Euler rétrograde euler_ret()

def euler_ret(f, t0, y0, T, N, eps_rel=1E-10, maxiter=500): 
    '''
    But : 
        résoudre résoudre un problème de Cauchy par la méthode d'Euler progressive
    Paramètres : 
        f : la pente (la dérivée) de la solution
        t0 : le moment initial
        y0 : la valeur initiale
        T : la durée d'étude
        N : le nombre de sous-intervalles
        eps_rel : la tolérance relative pour le problème non linéaire 
        maxiter : le nombre maximal d'itérations pour le problème non linéaire
    Retourne : 
        t : le vecteur (1D array) avec les points où la solution approchée a été calculée
        u : le vecteur (1D array) avec les valeurs approchées de la solution                 
    ''' 
    t, h = np.linspace(t0, T, N+1, retstep=True)
    u = np.empty(N+1)
    u[0] = y0 
    for n in range(N):        
        u_old = u[n] + h*f(t[n], u[n])
        u_new = u[n] + h*f(t[n+1], u_old)
        iter = 1
        while abs(u_new - u_old) > eps_rel*abs(u_new):
            u_old = u_new
            u_new = u[n] + h*f(t[n+1], u_old)
            iter += 1
            if iter > maxiter:
                raise Exception('Problème non linéaire non convergent !')
        u[n+1] = u_new
    return t, u 

#Schéma explicite à un pas de Runge-Kutta classique rk4()

def rk4(f, t0, y0, T, N): 
    '''
    But : 
        résoudre un problème de Cauchy par la méthode d'Euler progressive
    Paramètres : 
        f : la pente (la dérivée) de la solution
        t0 : le moment initial
        y0 : la valeur initiale
        T : la durée d'étude
        N : le nombre de sous-intervalles
    Retourne : 
        t : le vecteur (1D array) avec les points où la solution approchée a été calculée
        u : le vecteur (1D array) avec les valeurs approchées de la solution                   
    ''' 
    t, h = np.linspace(t0, T, N+1, retstep=True)
    u = np.empty(N+1)
    u[0] = y0  
    for n in range(N):
        k1 = f(t[n], u[n])
        k2 = f(t[n] + 0.5*h, u[n] + 0.5*h*k1)
        k3 = f(t[n] + 0.5*h, u[n] + 0.5*h*k2)
        k4 = f(t[n] + h, u[n] + h*k3)
        u[n+1] = u[n] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return t, u