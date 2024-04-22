#11
#Appel de fonction, changement de paramètres

def saluer(s1, s2='ton admirateur'):
    print(s1, 'de la part de', s2, '!')

formule = 'Bonsoir'
saluer(formule)
qui = 'moi'
saluer(formule, qui)

#Ne pas négliger l'importance des variables global

def calculer_moyenne():
    global poids1, poids2 
    poids1, poids2 = 0.4, 0.6
    def verifier():
        if poids1>0 and poids2>0 and poids1+poids2==1:
            return True
        else:
            return False    
    print('Dans la fonction : poids1 =', poids1, 'et poids2 =', poids2, '!')
    if verifier():
       return note1*poids1 + note2*poids2
    else:
       return note1*0.5 + note2*0.5
       
#la déclaration global dans "def" permet de modifier les variables au-delà de la fonction.

note1, note2, poids1, poids2 = 5, 6, .25, 0.75
print('La moyenne vaut:', calculer_moyenne(), '!')
print('Dans le module, après l\'appel : poids1 =', poids1, 'et poids2 =', poids2, '!')

#12
#Les fonctions peuvent s'appeler elle-même, c'est ce qu'on appelle la récursivité

def f(n):
    print("Je m'appelle moi-même (n = ", n, ") !", sep='')
    if n == 1:
        print('\nFin des appels (n = ', n, ') !', sep='')
        return
    f(n-1) #Appel récursif sans print !
    
print('\nStart')    
print(f(7))
print('\nOkay okay\n')

#13
#Déterminer l'âge d'une personne

def interagir():
    #Introduction des données
    print("\nBonjour ! C'est du code Python !")
    nom = input('Introduisez votre nom, svp :\n')
    prenom = input('Introduisez votre prénom, svp :\n')
    annee_naissance = input('Introduisez votre année de naissance, svp :\n')
    mois_naissance = input('Introduisez votre mois de naissance, svp :\n')
    return nom, prenom, annee_naissance,mois_naissance

    #Ne jamais oublier le return dans la fonction !
    #Attention à penser de déclarer annee_courant comme type "date.today().year"
def calculer_age(annee_naissance,mois_naissance):
    from datetime import date
    annee_courant = date.today().year
    mois_courant = date.today().month
    if int(annee_naissance) < 1900 or int(annee_naissance) > annee_courant:
        annee_naissance = 2000
        print("Attention : L'année de naissance remise par défaut à 2000 !")
    age = annee_courant - (annee_naissance)
    if mois_courant < int(mois_naissance):
        age -= 1
    return age

    #Il faut bien distinguer la fonction qui "déclare" et celle qui "calcule"
    #Puis mentionner quelle propriété appartient à quelle fonction !

nom, prenom, annee_naissance, mois_naissance = interagir()
print('Bonjour', prenom, nom, '!', '\nVous avez', calculer_age(annee_naissance,mois_naissance), 'ans !', '\nAu revoir !')

