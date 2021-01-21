"""
ceci est un programme qui affiche tous les caractères ayant un indice pair dans une
chaîne de caractères
"""
mot = input("Entrer un mot : ")
long_mot= len(mot)
for j in range(long_mot):
    #je verifie que l'indice est pair avant de l'afficher
    if j % 2 == 0:
        print(mot[j])
