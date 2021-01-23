"""
Soit le dictionnaire : d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}
a. Corriger l'erreur dans le prénom, la bonne valeur est 'Jacques'.
b. Afficher la liste des clés du dictionnaire.
c. Afficher la liste des valeurs du dictionnaire.
d. Afficher la liste des paires clé/valeur du dictionnaire.
e. Ecrire la phrase "Jacques Dupuis a 30 ans". 
"""
d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

#changer jacque par jacques
d['prenom']='Jacques'


print("\n\n")
print("affichage des clefs")
for i in d:
    print(i)


print("\n\n")
print("affichage des valeurs")
for j in d:
    print(" valeur : {}".format(d[j]))

print("\n\n")
print("affichage des clefs et valeurs")
for l in d:
    print("clef: {} : {}".format(l,d[l]))

print("\n\n")
print("Ecrire la phrase Jacques Dupuis a 30 ans \t")
print(d['prenom'], d['nom'], "a", d['age'],"ans")
