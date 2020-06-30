""""
Ecrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant
des astérisques entre les caractères.
Ainsi, par exemple, « Python » devra donner « P*y*t*h*o*n »
"""

nom = input("tapez un mot ")

#affichage en ajoutant * apres chaque caractere
print('*'.join(nom))