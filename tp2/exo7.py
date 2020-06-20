"""
ceci est une calculatrice
"""




#la fonction qui permet de changer d'operation durant le programme
def changer_options():
    changer = input("taper a pour faire une autre operation ou b pour quitter ")
    if changer == "a":
        menu()
    else:
        pass


#la fonction qui permet de faire l'addition
def addition():
    premier_valeur = int(input("Saisir premiere valeur "))
    deuxieme_valeur = int(input("Saisir premiere valeur "))
    print("La somme est ",premier_valeur + deuxieme_valeur)
    changer_options()



#la fonction qui permet de faire la soustraction
def soustraction():
    premier_valeur = int(input("Saisir premiere valeur "))
    deuxieme_valeur = int(input("Saisir premiere valeur "))
    print("La difference est ",premier_valeur - deuxieme_valeur)
    changer_options()


#la fonction qui permet de faire la multiplication
def multiplication():
    premier_valeur = int(input("Saisir premiere valeur "))
    deuxieme_valeur = int(input("Saisir premiere valeur "))
    print("Le produit est ",premier_valeur * deuxieme_valeur)
    changer_options()


#la fonction qui permet de faire la division
def division():
    premier_valeur = int(input("Saisir premiere valeur "))
    deuxieme_valeur = int(input("Saisir premiere valeur "))
    
    if deuxieme_valeur == 0:
        print("impossible de diviser par 0")
        menu()
    else:
        print("Le quotient est ",premier_valeur / deuxieme_valeur)
    changer_options()


#la fonction qui permet de faire le modulo
def modulo():
    premier_valeur = int(input("Saisir premiere valeur "))
    deuxieme_valeur = int(input("Saisir premiere valeur "))
    print("Le modulo est ",premier_valeur % deuxieme_valeur)
    changer_options()


#la fonction principale du programme
def menu():
    print("1-Addition")

    print("2-Soustraction")

    print("3-Multiplication")

    print("4-Division")

    print("5-Modulo")

    print("6-Quitter")

    
    choix = int(input("Faites votre choix "))


    if choix == 1:
        addition()

    elif choix == 2:
        soustraction()

    elif choix == 3:
        multiplication()

    elif choix == 4:
        division()

    elif choix == 5:
        modulo()

    elif choix == 6:
        pass

menu()












    





    
