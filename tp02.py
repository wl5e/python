#08
# Consigne : Démontrer que différentes variables peuvent avoir la même valeur mais des types et des identités différents.
print("Exercice 08 : Démontrer que différentes variables peuvent avoir la même valeur mais des types et des identités différents.")

x = 5
y = float(5)
z = 5.
t = complex(5)
u = '5'
# Affiche la valeur, le type et l'identité de chaque variable.
print(x)
print(type(x))
print(id(x))
print('\n*****************\n')
print(y)
print(type(y))
print(id(y))
print('\n*****************\n')
print(z)
print(type(z))
print(id(z))
print('\n*****************\n')
print(t)
print(type(t))
print(id(t))
print('\n*****************\n')
print(u)
print(type(u))
print(id(u))

#print(x, type(x), id(x))
#print(y, type(y), id(y))
#print(z, type(z), id(z))
#print(t, type(t), id(t))
#print(u, type(u), id(u))
#print('\n', '#' * 64, '\n')
#print('\n', '#' * 64, '\n')

# Consigne : Vérifier si un mot est un mot clé en Python.
print("\nExercice : Vérifier si un mot est un mot clé en Python.")
import keyword
# 'tata' n'est pas un mot clé, 'del' est un mot clé.
print(keyword.iskeyword('tata'))
print(keyword.iskeyword('del'))
#print(keyword.iskeyword(del))

# Consigne : Attribuer des valeurs à des variables.
print("\nExercice : Attribuer des valeurs à des variables.")
u, v = 3, 5
print('\nu =', u, 'et v=', v)
#La virgule met une séparation nette

# Consigne : Demandez à l'utilisateur d'entrer trois nombres réels et utilisez une structure conditionnelle pour les comparer.
print("\nExercice 09 : Demandez à l'utilisateur d'entrer trois nombres réels et utilisez une structure conditionnelle pour les comparer.")
a = float(input('\nEntrez un premier nombre réel :'))
b = float(input('\nEntrez un second nombre réel :'))
c = float(input('\nEntrez un dernier nombre réel :'))

# Consigne : Comparez trois nombres réels entrés par l'utilisateur et affichez le plus grand.
print("\nExercice : Comparez trois nombres réels entrés par l'utilisateur et affichez le plus grand.")
if a > b:
    if a > c:
        max = a
    else:
        max = c

else:
    if b > c:
        max = b
    else:
        max = c

print('\nLa plus grande valeur aue vous ayez rentré est :', max, " !\n")
print('\n', '#' * 64, '\n')

#10
# Consigne : Résolvez l'équation quadratique (viète)
print("\nExercice 10 : Résolvez l'équation quadratique (viète)")
print('\nVous avez une équation sous cette forme : ax^2 + bx + c) = 0')

a = float(input('\nentrez votre "a" :'))
b = float(input('entrez votre "b" :'))
c = float(input('entrez votre "c" :'))

det = float(b**2 - 4*a*c)
print ('\nle déterminant vaut :',det)


if det < 0  :
    print( '\nc est mort !')

elif det == 0 :
    result = (-b + det**(1/2))
    print('\nIl y a une solution :', result)
# possibilité d'utiliser math.sqrt()

elif det > 0 :
    result1 = (-b + det**(1/2))/(2*a)
    result2 = (-b - det**(1/2))/(2*a)
    print('\nIl y a deux solutions à l équation : ', result1, ' et ', result2)
print('\n', '#' * 64, '\n')

#11
# Consigne : Calculez la moyenne non pondérée des notes entrées par l'utilisateur.
print("\nExercice 11 : Calculez la moyenne non pondérée des notes entrées par l'utilisateur.")
print("\nLe programme calcule la moyenne des notes entrées par l'utilisateur !")
val = float(input('\nEntrez votre première note svp :'))
moyenne = val
nbr_notes = 1

# Dans un premier temps, on considère qu'on ne rentre qu'une seule note.

iterations = input(
    '\nVous avez entré la première note, voulez-vous en introduire une autre ?\n'
    '(Oui/ Non)')
if iterations == 'oui' or iterations == 'Oui' or iterations =='yes' or iterations == 'Yes' or iterations == 'Oui.' or iterations == 'OUI':
    get = True
else:
    get = False

# Première itération
# On fait appelle à une fonctione booléenne "true or false"

while get:
    val = float(input('Entrez la note suivante, svp :'))
    moyenne += val
    nbr_notes += 1
    iterations = input(
    '\nVous avez entré la première note, voulez-vous en introduire une autre ?\n'
    '(Oui/ Non)')
    if iterations == 'oui' or iterations == 'Oui' or iterations =='yes' or iterations == 'Yes' or iterations == 'ui':
        get = True
    else:
        get = False

# Aussi longtemps que la booléenne est vrai, la moyenne additionne des notes
# et le nombre de notes fait +1
# La question sera reposée encore et encore ...

moyenne /= nbr_notes
print('\nLa moyenne des ', nbr_notes, 'notes que vous avez introduit est :',
moyenne, ' ! c:')

#calcul non pondéré d'une moyenne   