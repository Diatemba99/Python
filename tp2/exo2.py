"""
ceci est un script qui  affiche et incrémentant la valeur de a tant qu’elle reste inférieure
à celle de b.
Mais également  décrémente la valeur de b et affichant sa valeur si elle est
impaire. Boucler tant que b n’est pas nul.

"""
a, b = 0, 10

print("boucle ++ ")
while a <= b:
    print(a, end=' ')
    a+= 1
    
#boucle qui decremente en affichant les valeurs impaires
print("\n\n" +"Boucle --")
for i in range(1,b):
        if i % 2 != 0:
            print(b-i, end=' ')
