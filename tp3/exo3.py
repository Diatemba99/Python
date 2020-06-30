""""
Considérez une chaîne de caractères saisie au clavier par l’utilisateur contenant une
liste de noms de diverses sociétés multinationales. Utilisez la méthode split() pour
convertir la chaîne en une liste de sous-chaînes puis afficher chaque sous-chaîne sur
une nouvelle ligne différente
"""


list_des_firmes = input("taper votre liste de firmes ")

#je transforme la variable en tabeau
afficher_liste = list_des_firmes.split()


#je supprime le dernier elmt du tableau que je stocke dans une variable
dernier_element_liste = afficher_liste.pop()


#je cree un tableau pour contenir chaque elmt du tableau dans une boucle
contenaire_element_firme = []


for i in afficher_liste:

    #je stocke chaque element du tableau dans une variable
    contenaire_element_firme = i

    #je stocke le nom de la firme avant la virgule
    un_element_contenaire = contenaire_element_firme[0:len(i)-1]

    #j'affiche le nom de la firme sans la virgule
    print(un_element_contenaire)


#j'affiche le dernier element du tableau que j'avais supprimé
print(dernier_element_liste)


